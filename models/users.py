import pydantic


class Credentials(pydantic.BaseModel):
    username: str
    password: str


class User(pydantic.BaseModel):
    id: int
    username: str


class UserUpdate(pydantic.BaseModel):
    auth: Credentials
    username: str
