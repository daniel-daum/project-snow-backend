from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class ResortBase(BaseModel):

    id: int
    name: str
    city: str
    state: str
    latitude: float
    longitude: float
    last_modified_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class addToken(BaseModel):
    token: str
    users_id = int

    class Config:
        orm_mode = True


class getBlackJWT(addToken):
    created_at: datetime
    id: int

    class Config:
        orm_mode = True


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


class CreateUserVerified(CreateUser):
    email_verified: bool

    class Config:
        orm_mode = True


# User Response Schema
class User(UserBase):
    id: int
    created_at: datetime
    email_verified: Optional[bool]

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None
    users_email: Optional[str] = None


# Create Role  Schema and Response


class CreateRole(BaseModel):
    """Create a Role Schema"""

    users_id: int
    role: str
    admin_created_by: str

    class Config:
        orm_mode = True


class GetRoleResponse(CreateRole):
    """Create a Role response Schema"""

    created_at: datetime

    class Config:
        orm_mode = True


class EmailVerify(BaseModel):
    id: int
    temp_jwt: str
    users_id: int
    users_email: str

    class Config:
        orm_mode = True


class EmailVerifyResponse(EmailVerify):
    created_at: datetime

    class Config:
        orm_mode = True
