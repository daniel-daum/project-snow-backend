from sqlalchemy.orm import Session
from datetime import datetime
from ..database import models, schemas
from . import utils


def get_user_by_id(db: Session, id: int):
    """Returns a single user based on id."""

    return db.query(models.User).filter(models.User.id == id).first()

# GET ONE USER BY EMAIL
def get_user_by_email(db: Session, user: schemas.CreateUser):
    """Returns a single user based on email."""

    return db.query(models.User).filter(models.User.email == user.email).first()


# CREATE NEW USER
def create_user(db: Session, user: schemas.CreateUser):
    """Creates a new user in the database."""

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# DELETE A USER
def delete_user(db: Session, user: schemas.User):
    """Deletes a user in the database based on id."""

    db.delete(user)
    db.commit()

    return None

def update_last_login(db: Session, user_id: int):

    current_datetime = datetime.now()

    db.query(models.User).filter(models.User.id == user_id).update(
        {models.User.last_login: current_datetime})

    db.commit()

    return get_user_by_id(db, user_id)