from models import Task, TaskCreate, SubTask, SubTaskCreate
from database import database, get_task, get_subtask


class TaskService:
    def __init__(self) -> None:
        self.task_data: list[Task] = []
        self.subtasks_data: list[SubTask] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        tasks_data = database.get_tasks_db()
        tasks = []
        for item in tasks_data:
            tasks.append(get_task(item))
        self.task_data = tasks

    def load_subtasks(self) -> None:
        subtasks_data = database.get_subtasks_db()
        subtasks = []
        for item in subtasks_data:
            subtasks.append(get_subtask(item))
        self.subtasks_data = subtasks

    def get_tasks(self) -> list[Task]:
        self.load_tasks()
        return self.task_data

    def get_subtasks(self) -> list[SubTask]:
        self.load_subtasks()
        return self.subtasks_data


task_service: TaskService = TaskService()
