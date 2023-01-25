from sqlalchemy.orm import Session
from ..database import models, schemas


# CREATE NEW USER ROLE
def create_role(db: Session, role: schemas.CreateRole):
    """Adds a 'role' to a user in the roles table. i.e. User or Admin"""

    new_role = models.User_Roles(**role)

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role
