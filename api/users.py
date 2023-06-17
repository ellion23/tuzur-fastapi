from fastapi import APIRouter, HTTPException
from database import database
from models import User, UserUpdate, Credentials, RestoreData
from services import user_service, email_service
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
    "/users/{id}/update",
    response_model=User,
)
async def update_user(
        id: int,
        data: UserUpdate
):
    return user_service.update_user(id=id, payload=data)


@router.get(
    "/users/get_restore_code",
    response_model=str,
)
async def get_restore_code(email: str):
    users = user_service.get_users()
    for user in users:
        if user.email == email:
            code_str = f"{randint(1, 9999):4d}"
            code_db = RestoreData(email=email, code=code_str)
            database.write_code(code_db)
            email_service.send_restore_code(code_db.email, code_str)
            return email
    raise HTTPException(status_code=400, detail="No user with this Email address")


@router.put(
    "/users/restore",
    response_model=User
)
async def restore_user(data: RestoreData, password: str):
    if database.redeem_code(data):
        return database.restore_user_db(data, password)
    else:
        raise HTTPException(status_code=400, detail="Incorrect code")
