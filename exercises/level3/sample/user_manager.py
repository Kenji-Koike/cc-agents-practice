class User:
    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r}, age={self.age})"


class UserManager:
    def __init__(self):
        self._users: dict[str, User] = {}

    def add_user(self, user: User):
        # バグ: email の重複チェックなし
        # バグ: age のバリデーションなし（負の値や200歳も通る）
        self._users[user.email] = user

    def get_user(self, email: str) -> User:
        # バグ: 存在しない場合の処理なし（KeyError が発生する）
        return self._users[email]

    def list_users(self) -> list:
        return list(self._users.values())
