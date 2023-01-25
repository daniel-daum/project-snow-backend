from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Date, null, Boolean, Float
from sqlalchemy.sql.expression import text

class Resort(Base):
    __tablename__ = "resorts"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    last_modified_at = Column(TIMESTAMP(timezone=True))

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True



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

    class Config:
        orm_mode = True

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    last_login = Column(TIMESTAMP(timezone=True))
    email_verified = Column(Boolean, default=False)

    class Config:
        orm_mode = True


class Email_Verification(Base):
    __tablename__ = "email_verification"

    id = Column(Integer, primary_key=True, nullable=False)
    temp_jwt = Column(String(255), nullable=False)
    users_id = Column(Integer, nullable=False)
    users_email = Column(String(100), ForeignKey(
        "users.email"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    class Config:
        orm_mode = True

class User_Roles(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"))
    role = Column(String(255), nullable=False)
    admin_created_by = Column(String(255))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    class Config:
        orm_mode = True

class Token_list(Base):
    __tablename__ = "generated_tokens"

    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(255), nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    class Config:
        orm_mode = True