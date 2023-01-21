from pydantic import BaseModel
from datetime import datetime


class ResortBase(BaseModel):

    id: int
    name:str
    city:str
    state:str
    latitude:float
    longitude:float
    last_modified_at:datetime

    class Config:
        orm_mode = True
