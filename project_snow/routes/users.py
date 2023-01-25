from fastapi import APIRouter, Depends, HTTPException, status
from project_snow.database import schemas
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..utilities import users_crud, oauth2

router = APIRouter(tags=["Users"], prefix="/api/users")


# CREATE A NEW USER
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User, tags=["Users"])
async def create_new_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    """Creates a new user in the database."""

    db_user = users_crud.get_user_by_email(db, user)

    # checks if user already exists in the database.
    if db_user is None:

        # CREATES A NEW USER IN THE DB
        new_user = users_crud.create_user(db, user)

        # CREATES A JWT FOR EMAIL VERIFICATION
        token = oauth2.create_access_token(
            data={"user_id": new_user.id, "users_email": new_user.email})

        # # SENDS AN EMAIL WITH THE JWT
        # crud.send_verification_email(db, token, new_user)

    else:
        raise HTTPException(
            status_code=400, detail="Email already registered")

    return new_user