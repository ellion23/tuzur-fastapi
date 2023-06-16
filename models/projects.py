from typing import List
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    owner_id: int
    title: str


class Project(BaseModel):
    proj_id: int
    owner_id: int
    title: str
    tasks: List[int] | None = None
