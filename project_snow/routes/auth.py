from fastapi import APIRouter, Depends, HTTPException, status
from project_snow.database import schemas
from sqlalchemy.orm import Session
from ..database.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import models
from ..utilities import utils, oauth2, token_crud, users_crud, roles_crud
from fastapi.responses import HTMLResponse


router = APIRouter(tags=["Authentication"], prefix="/api/auth")


@router.post("/login", tags=["Authentication"], response_model=schemas.Token)
async def authenticate(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Authenticates user credentials and generates a JWT"""

    unauthenticated_user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if unauthenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password, unauthenticated_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    authenticated_user = unauthenticated_user

    # CREATE AN ACCESS TOKEN
    access_token = oauth2.create_access_token(data={"user_id": authenticated_user.id})


    # Add TOKEN TO BLACKLIST TABLE
    blacklist_token = {"token": access_token, "users_id": authenticated_user.id}
    token_crud.add_token_to_blist(db, blacklist_token)


    # UPDATE USERS LAST LOGIN
    users_crud.update_last_login(db, authenticated_user.id)

    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/verify_email/{token}", tags=["Authentication"], response_class=HTMLResponse)
async def verify_email(token: str, db: Session = Depends(get_db)):

    # Create a credentials exception
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate email credentials", headers={"WWW-Authenticate": "Bearer"})

    # Recieve, deconstruct, verify token is valid
    payload = oauth2.verify_access_token(token, credentials_exception)

    # Update email verified column to True
    db.query(models.User).filter(models.User.id == payload.id).update(
        {models.User.email_verified: True}, synchronize_session=False)
    db.commit()

    user = users_crud.get_user_by_id(db, payload.id)

    # Give user permissions in permissions table after email is verfied
    role_data = {"users_id": payload.id, "role": f"user",
                 "admin_created_by": f"daniel"}

    # Give account user level permissions
    roles_crud.create_role(db, role_data)


    db.query(models.User).filter(models.User.id == payload.id).update(
        {models.User.email_verified: True}, synchronize_session=False)
    db.commit()


    blacklist_token = {"token": token, "users_id": user.id}

    # Add TOKEN TO BLACKLIST TABLE
    token_crud.add_token_to_blist(db, blacklist_token)

    return """
   <!DOCTYPE html>
   <html lang="en">
   <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Verified</title>
    </head>
    <body style="width:100vw; height: 100vh; margin: 0px; padding:0px; display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: #F6F9FC;">
        <div style="  background: -webkit-linear-gradient(45deg, #1171ef, #17c8eb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: .2em; font-style: italic; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; align-self: center; margin-bottom: .25em; font-size: 3em;">SNOWFALL</div>
        <div style="box-shadow: 0 1px 3px rgba(50, 50, 93, .15), 0 1px 0 rgba(0, 0, 0, .02);border-radius: .3em; border: 1px solid #1171ef; width: fit-content; background-color:#1171ef; display: flex; flex-direction: column; align-items: center; justify-content:center;">
        <p style=" color: white; width: fit-content; letter-spacing: .1em; font-size: 1em; padding: 1em; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-weight: 600; ">You have successfully verified your email!</p>
    </div>
    </body>
    </html>
        """