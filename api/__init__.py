from fastapi import APIRouter

from api.users import router as user_router
from api.projects import router as proj_router
from api.tasks import router as task_router

router = APIRouter()

router.include_router(user_router)
router.include_router(proj_router)
router.include_router(task_router)
