from fastapi import APIRouter, HTTPException
from models import User, UserUpdate, Credentials
from services import UserService, user_service
from database import get_users_db

router = APIRouter()


@router.post("/users/register",
             response_model=User,
             )
async def register_user(creds: Credentials):
    users = user_service.get_users()
    for user in users:
        if user.email == creds.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    newUser = user_service.register(creds)
    return newUser


@router.get(
    "/users",
    status_code=200,
    response_model=list[User],
)
async def get_users():
    return user_service.get_users()


@router.get(
    "/users/login/",
    status_code=200,
    response_model=User
)
async def login(email: str, password: str):
    user = user_service.auth(Credentials(email=email, password=password))
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="Incorrect email/password")


@router.put(
    "/users/{id}",
    response_model=User,
)
async def update_user(
        id: int,
        data: UserUpdate
):
    return user_service.update_user(id=id, payload=data)
