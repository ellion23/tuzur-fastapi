from pydantic import BaseModel


class SubTaskCreate(BaseModel):
    task_id: int
    owner_id: int
    title: str
    importance: int
    executor: str
    description: str | None = None


class SubTask(BaseModel):
    id: int
    owner_id: int
    title: str
    importance: int
    executor: str
    description: str | None = None
    task_id: int
