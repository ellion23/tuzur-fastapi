from pydantic import BaseModel


class Credentials(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    username: str


class UserUpdate(BaseModel):
    auth: Credentials
    username: str
