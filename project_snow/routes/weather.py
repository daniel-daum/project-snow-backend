from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..utilities.weather_crud import get_resorts_daily_weather, get_resorts_hourly_weather


router = APIRouter(tags=["Weather"], prefix="/api/weather")


@router.get("/daily/{id}")
async def resort_daily_weather(id:int, db: Session = Depends(get_db)):
    """Returns weather for a specific resort based upon its id."""

    resort_weather =  get_resorts_daily_weather(db, id)

    if resort_weather is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no daily weather report for this resort in the database.",
        )

    return resort_weather


@router.get("/weekly/{id}")
async def resort_hourly_weather(id:int, db: Session = Depends(get_db)):
    """Returns weather for a specific resort based upon its id."""

    resort_weather =  get_resorts_hourly_weather(db, id)

    if resort_weather is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no hourly weather report for this resort in the database.",
        )

    return resort_weather

