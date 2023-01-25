from fastapi import APIRouter, Depends, HTTPException, status
from project_snow.database import schemas
from sqlalchemy.orm import Session
from ..database.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import models
from ..utilities import utils, oauth2, token_crud, users_crud


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