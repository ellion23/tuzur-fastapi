from fastapi import APIRouter
from schemas.users import User, UserUpdate, Credentials
from services.users import user_service

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
    return user_service.get_users()

@router.put(
    "/users/{id}",
    response_model=User,
)
def update_user(
        id: int,
        data: UserUpdate
):
    return user_service.update_user(id=id, payload=data)
