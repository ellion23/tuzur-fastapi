from models import User, UserUpdate, Credentials
from database import get_users_db, add_user, User_db, Item_db, get_hash, update_user_db


class UserService:
    def __init__(self) -> None:
        self.user_data: list[User] = []
        self.load_users()

    def load_users(self) -> None:
        user_data = get_users_db()
        items = []

        for item in user_data:
            items.append(
                User(
                    id=item.id,
                    username=item.username,
                    email=item.email,
                    hashed_password=item.hashed_password
                )
            )
        self.user_data = items

    def get_users(self) -> list[User]:
        self.load_users()
        return self.user_data

    def update_user(self, id: id, payload: UserUpdate) -> User:
        if auth_user := self.auth(payload.auth):
            if auth_user.id != id:
                raise ValueError("User does not exists") # ???

            for item in self.user_data:
                if item.email == payload.auth.email:
                    item.username = payload.username
                    update_user_db(item)
                    return item
            raise ValueError("Нету шомны")

    def register(self, payload: Credentials) -> User:
        return add_user(payload)

    def auth(self, credentials: Credentials):
        for item in self.user_data:
            if item.email == credentials.email and item.hashed_password == get_hash(credentials.password):
                return item  # What?
        return None


user_service: UserService = UserService()
