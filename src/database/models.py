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