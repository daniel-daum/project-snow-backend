import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv("./.env")


class Settings(BaseSettings):

    DBSTR: str =os.getenv("DBSTR")

    KEY: str = os.getenv("KEY")
    ALGO: str = os.getenv("ALGO")
    EXPIRE: str = os.getenv("EXPIRE")

    EMAIL: str = os.getenv("EMAIL")
    EMAIL_SERVER: str = os.getenv("EMAIL_SERVER")
    EMAIL_SERVER_KEY: str = os.getenv("EMAIL_SERVER_KEY")

    DEPLOYMENT_ENV: str = os.getenv("DEPLOYMENT_ENV")


settings = Settings()
