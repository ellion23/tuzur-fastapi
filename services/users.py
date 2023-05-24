from models import User, UserUpdate, Credentials

import uuid
#
# user_data: list[dict] = [
#     {
#         'id': 1,
#         "username": 'Allah',
#         'role': 'admin',
#         "password": '11111111'
#     },
#     {
#         'id': 2,
#         'username': 'Jesus',
#         'role': 'client',
#         'password': 'TheBestPasswordOfEver'
#     }
# ]


class UserService:
    def __init__(self, user_data: list[dict]) -> None:
        self.user_data = user_data

    def get_users(self) -> list[User]:
        items = []

        for item in self.user_data:
            items.append(
                User(
                    id=item['id'],
                    username=item['username']
                )
            )

        return items

    def update_user(self, id: int, payload: UserUpdate) -> User:
        if auth_user := self._auth(payload.auth):
            if auth_user.id != id:
                raise ValueError("Шомны нет")

            for item in self.user_data:
                if item["id"] == id:
                    item['username'] = payload.username

                    return User(
                        id=item["id"],
                        username=item["username"]
                    )
            raise ValueError("Нету шомны")

    def register(self, payload: Credentials) -> User:
        self.user_data.append({
            "id": uuid.uuid4(),
            "username": payload.username,
            'TOWRITE': "TOWRITE" # TODOsss
        })

    def _auth(self, credentials: Credentials):
        for item in self.user_data:
            if item['username'] == credentials.username and item['password'] == credentials.password:
                return User(id=item["id"], username=item["username"])
        return None


# user_service: UserService = UserService(user_data)
