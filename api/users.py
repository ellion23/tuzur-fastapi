from fastapi import APIRouter
from models import User, UserUpdate, Credentials
from services import UserService
from database import get_users_db

router = APIRouter()

@router.post("/users", response_model=User,)
def register_user(data: Credentials):
    pass

@router.get(
    "/users",
    status_code=200,
    response_model=list[User],
)
def get_users():
    # return user_service.get_users()
    return None
    # TODO: work with database

@router.put(
    "/users/{id}",
    response_model=User,
)
def update_user(
        id: int,
        data: UserUpdate
):
    # return user_service.update_user(id=id, payload=data)
    return None
    # TODO: work with database

@router.get(
    "/test1/",
    status_code=200,
)
async def test1():
    return get_users_db()
