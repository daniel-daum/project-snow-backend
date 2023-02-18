
from datetime import datetime

from sqlalchemy.orm import Session

from ..database import models


def get_resorts_daily_weather(db: Session, id:int):
    """Returns the weather for a single resort"""

    return db.query(models.Daily_forecast).filter(models.Daily_forecast.resort_id == id).first()


def get_resorts_hourly_weather(db: Session, id:int):
    """Returns the weather for a single resort"""

    return db.query(models.Hourly_forecast).filter(models.Hourly_forecast.resort_id == id).first()