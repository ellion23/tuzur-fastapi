from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/items",
    status_code=200
)

def get_items():
    pass
