from sqlalchemy.orm import Session
from ..database import models
from datetime import datetime



def get_all_resorts(db: Session):
    """Returns all resorts in the database."""

    return db.query(models.Resort).all()
    

def get_resort_by_id(db:Session, id:int):
    """Returns a resort based on its id."""

    return db.query(models.Resort).filter(models.Resort.id == id).first()


def update_supply_last_modified(db: Session, resort_id: int):

    current_datetime = datetime.now()

    db.query(models.Resort).filter(models.Resort.id == resort_id).update(
        {models.Resort.last_modified_at: current_datetime})

    db.commit()

    return get_resort_by_id(db, resort_id)