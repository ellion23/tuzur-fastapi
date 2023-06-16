from fastapi import APIRouter

from api.users import router as user_router
from api.items import router as item_router
from api.projects import router as proj_router

router = APIRouter()

router.include_router(user_router)
router.include_router(item_router)
router.include_router(proj_router)
