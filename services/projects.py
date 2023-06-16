from models import Project, ProjectCreate
from database import database


class ProjectService:
    def __init__(self) -> None:
        self.user_data: list[Project] = []
        self.load_projects()

    def load_projects(self) -> None:
        user_data = database.get_users_db()
        items = []

        for item in user_data:
            items.append(
                User(
                    id=item.id,
                    username=item.username,
                    email=item.email,
                    hashed_password=item.hashed_password
                )
            )
        self.user_data = items
