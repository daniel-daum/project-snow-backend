from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


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



class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class addToken(BaseModel):
    token: str
    users_id = int


class getBlackJWT(addToken):
    created_at: datetime
    id: int


# Base User Schema
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    
    class Config:
        orm_mode = True

class CreateUser(UserBase):
    password: str

    class Config:
        orm_mode = True


# User Response Schema
class User(UserBase):
    id: int
    created_at: datetime
    email_verified: Optional[bool]

    class Config:
        orm_mode = True