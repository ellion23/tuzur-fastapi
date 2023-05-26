from fastapi import APIRouter, HTTPException
from models import User, UserUpdate, Credentials, RestoreCode, RestoreData
from services import UserService, user_service, email_service
from database import database
from random import randint

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


@router.get(
    "/users/get_restore_code",
    response_model=RestoreCode,
)
def send_code(data: RestoreData):
    users = user_service.get_users()
    for user in users:
        if user.email == data.email:
            return RestoreCode(code=f"{randint(1, 9999):04d}")
    raise HTTPException(status_code=400, detail="No user with this Email address")


@router.put(
    "/users/restore",
    response_model=Credentials
)
def restore_user():
    pass  # TODO: Restoration


@router.get(
    "/users/test"
)
def test1():
    try:
        email_service.send_restore_code(dest_email="rubcinskija@gmail.com", code=f"{randint(1, 9999):04d}")
        return {"message": "access"}
    except:
        raise HTTPException(status_code=400, detail="Error")
