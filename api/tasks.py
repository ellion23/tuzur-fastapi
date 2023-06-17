from fastapi import APIRouter
from database import database
from models import User, UserUpdate, Credentials, RestoreData, Task, TaskCreate, SubTaskCreate, SubTask
from services import user_service, email_service, project_service, task_service
from random import randint

router = APIRouter()


@router.get(
    "/tasks",
    status_code=200
)
async def get_tasks():
    return task_service.get_tasks()


@router.get(
    "/subtasks",
    status_code=200
)
async def get_tasks():
    return task_service.get_subtasks()


@router.post(
    "/add_task",
    status_code=200
)
async def add_task(task: TaskCreate):
    return database.add_task_db(task)


@router.post(
    "/add_subtask",
    status_code=200
)
async def add_subtask(task: SubTaskCreate):
    return database.add_subtask_db(task)


@router.put(
    "/update_task",
    status_code=200
)
async def update_task(task: Task):
    return database.update_task(task)


@router.put(
    "/update_subtask",
    status_code=200
)
async def update_subtask(task: SubTask):
    return database.update_subtask(task)
