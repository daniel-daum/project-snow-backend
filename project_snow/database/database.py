from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from project_snow.settings import settings

Base = declarative_base()

engine = create_engine(settings.DBSTR)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()