from fastapi import APIRouter
from database import database
from models import User, UserUpdate, Credentials, RestoreData, ProjectCreate, Project
from services import user_service, email_service
from random import randint

router = APIRouter()

@router.get(
    "/projects",
    status_code=200
)
def get_projects():
    pass

@router.post(
    "/add_project",
    status_code=200
)
def add_project(proj: ProjectCreate):
    return database.add_project(proj)


