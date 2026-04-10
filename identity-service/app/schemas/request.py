from pydantic import BaseModel
from typing import Optional


class SignUpRequest(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class ResetPwdRequest(BaseModel):
    username: str
    new_password: str


class GetUserInfoRequest(BaseModel):
    username: str


class LoginRequest(BaseModel):
    username: str
    password: str
