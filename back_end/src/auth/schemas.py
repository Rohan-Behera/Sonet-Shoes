from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class TokenDetailsModel(BaseModel):
    user_details: dict
    exp: float
    type: str
    refresh : bool
    jti: str

class UserCreateModel(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str = Field(max_length = 40)
    password: str = Field(min_length = 8)

class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    password: str = Field(exclude=True) #excludes the password to be returned in response
    email:str
    first_name: str
    last_name: str
    is_verified: bool 
    created_on: datetime
    modify_on: datetime

class UserLoginModel(BaseModel):
    email: str = Field(max_length = 40)
    password: str = Field(min_length = 8)

class EmailModel(BaseModel):
    addresses: list[str]

class PasswordRequestModel(BaseModel):
    email: str

class PasswordResetConfirmModel(BaseModel):
    new_password: str
    confirm_password: str

class UserResponseModel(BaseModel):
    email: str
    uid: uuid.UUID

class LoginResponseModel(BaseModel):
    message: str
    access_token: str
    refresh_token: str
    user: UserResponseModel