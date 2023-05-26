from pydantic import BaseModel, EmailStr


class Credentials(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: int
    username: str | None = None
    email: EmailStr
    hashed_password: str


class UserUpdate(BaseModel):
    auth: Credentials
    username: str
