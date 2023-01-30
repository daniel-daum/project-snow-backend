from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from project_snow.database import schemas

from ..database.database import get_db
from ..utilities import oauth2, users_crud, utils

router = APIRouter(tags=["Users"], prefix="/api/users")


# CREATE A NEW USER
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User,
    tags=["Users"],
)
# , current_user_id: int = Depends(oauth2.get_current_user)
async def create_new_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    """Creates a new user in the database."""

    db_user = users_crud.get_user_by_email(db, user)

    # checks if user already exists in the database.
    if db_user is None:

        # CREATES A NEW USER IN THE DB
        # new_user = users_crud.create_user(db, user)

        # CREATEA A NEW USER IN THE UNACTIVATED USER ACCOUNT DB
        new_user = users_crud.create_unactivated_user(db, user)

        # CREATES A JWT FOR EMAIL VERIFICATION
        token = oauth2.create_access_token(
            data={"user_id": new_user.id, "users_email": new_user.email}
        )

        # SENDS AN EMAIL WITH THE JWT
        utils.send_verification_email(db, token, new_user)

    else:
        raise HTTPException(status_code=400, detail="Email already registered")

    return new_user
