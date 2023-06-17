from typing import List
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    owner_id: int
    title: str
    description: str | None = None


class Project(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    tasks: str | None = None
