from sqlalchemy.orm import Session
from ..database import models



def get_all_resorts(db: Session):
    """Returns all resorts in the database."""

    return db.query(models.Resort).all()