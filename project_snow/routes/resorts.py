from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import schemas
from ..database.database import get_db
from ..utilities import oauth2
from ..utilities.resorts_crud import get_all_resorts, get_resort_by_id

router = APIRouter(tags=["Resorts"], prefix="/api/resorts")


# , current_user_id: int = Depends(oauth2.get_current_user)
# Get a list of the resorts
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ResortBase],
    tags=["Resorts"],
)
async def resorts(db: Session = Depends(get_db)):
    """Returns a list of all the resorts in the database."""

    resorts: list = get_all_resorts(db)

    if resorts == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no resorts in the database.",
        )

    return resorts


#     current_user_id: int = Depends(oauth2.get_current_user)
# Return one resort
@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ResortBase,
    tags=["Resorts"],
)
async def resort(
    id: int,
    db: Session = Depends(get_db),
):
    """Returns a single resort based on its id."""

    resort = get_resort_by_id(db, id)

    if resort is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resort with id: {id} was not found",
        )

    return resort
