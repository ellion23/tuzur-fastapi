from fastapi import APIRouter
from database import database
from models import User, UserUpdate, Credentials, RestoreData, ProjectCreate, Project
from services import user_service, email_service, project_service
from random import randint

router = APIRouter()


@router.get(
    "/projects",
    status_code=200
)
async def get_projects():
    return project_service.get_projects()


@router.post(
    "/add_project",
    status_code=200
)
async def add_project(proj: ProjectCreate):
    return database.add_project(proj)


@router.put(
    "/update_project",
    status_code=200
)
async def update_project(proj: Project):
    return database.update_project(proj)
