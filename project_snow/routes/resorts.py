from fastapi import APIRouter, status, Depends, HTTPException
from ..database import schemas
from typing import List
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..utilities.resorts_crud import get_all_resorts


router = APIRouter(tags=["Resorts"], prefix="/api/resorts")


# Get a list of the resorts
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResortBase], tags=["Resorts"])
async def list_resorts(db: Session = Depends(get_db)):
    """Returns a list of all the resorts in the database."""

    resorts:list = get_all_resorts(db)

    if resorts == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no resorts in the database.")

    return resorts

