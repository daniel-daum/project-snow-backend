from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Date, null, Boolean, Float

class Resort(Base):
    __tablename__ = "resorts"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    last_modified_at = Column(TIMESTAMP(timezone=True))


class Daily_forecast(Base):
    __tablename__ = "daily_forecast"

    id = Column(Integer, primary_key=True, nullable=False)
    resort_id = Column(Integer, ForeignKey("resorts.id"), nullable=False)
    period = Column(Integer, nullable=False)
    relative_date = Column(String(50))
    start_time = Column(Date, nullable=False)
    end_time = Column(Date, nullable=False)
    is_daytime = Column(Boolean)
    temperature = Column(Integer)
    temperature_unit = Column(String(1))
    temperature_trend = Column(String(255))
    wind_speed = Column(String(100))
    wind_direction = Column(String(5))
    icon = Column(String)
    short_forecast = Column(String(50))
    detailed_forecast = Column(String(100))

    last_updated_at = Column(TIMESTAMP(timezone=True))
    valid_from = Column(TIMESTAMP(timezone=True))
    valid_to = Column(TIMESTAMP(timezone=True))



class Hourly_forecast(Base):
    __tablename__ = "hourly_forecast"

    id = Column(Integer, primary_key=True, nullable=False)
    resort_id = Column(Integer, ForeignKey("resorts.id"), nullable=False)
    period = Column(Integer, nullable=False)
    relative_date = Column(String(50))
    start_time = Column(Date, nullable=False)
    end_time = Column(Date, nullable=False)
    is_daytime = Column(Boolean)
    temperature = Column(Integer)
    temperature_unit = Column(String(1))
    temperature_trend = Column(String(255))
    wind_speed = Column(String(100))
    wind_direction = Column(String(5))
    icon = Column(String)
    short_forecast = Column(String(50))
    detailed_forecast = Column(String(100))

    last_updated_at = Column(TIMESTAMP(timezone=True))
    valid_from = Column(TIMESTAMP(timezone=True))
    valid_to = Column(TIMESTAMP(timezone=True))

