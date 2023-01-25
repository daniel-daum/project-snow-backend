from sqlalchemy.orm import Session

from ..database import models, schemas


def add_token_to_blist(db: Session, token: schemas.addToken):

    issued_token = models.Token_list(**token)

    db.add(issued_token)
    db.commit()
    db.refresh(issued_token)

    return issued_token
