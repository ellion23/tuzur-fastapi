from fastapi import APIRouter
from models import User, UserUpdate, Credentials
from services import UserService
from database import get_users_db

router = APIRouter()


@router.post("/users/new",
             # response_model=User,
             )
def register_user(creds: Credentials):
    users = get_users_db()
    for user in users:
        print(user.email, creds.email)
        if user.email == creds.email:
            return "User already exists"


@router.get(
    "/users",
    status_code=200,
    # response_model=list[User],
)
def get_users():
    # return user_service.get_users()
    return get_users_db()
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
