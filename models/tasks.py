from pydantic import BaseModel


class TaskCreate(BaseModel):
    owner_id: int
    title: str
    importance: int
    executor: str
    description: str | None = None


class Task(BaseModel):
    id: int
    owner_id: int
    title: str
    importance: int
    executor: str
    description: str | None = None
