from models import Project, ProjectCreate
from database import database


class ProjectService:
    def __init__(self) -> None:
        self.project_data: list[Project] = []
        self.load_projects()

    def load_projects(self) -> None:
        project_data = database.get_projects_db()
        items = []

        for item in project_data:
            tasks = None
            if item.tasks:
                tasks = item.tasks.split(",")
            items.append(
                Project(
                    id=item.id,
                    owner_id=item.owner_id,
                    title=item.title,
                    description=item.description,
                    tasks=tasks
                )
            )
        self.project_data = items

    def get_projects(self) -> list[Project]:
        self.load_projects()
        return self.project_data


project_service: ProjectService = ProjectService()
