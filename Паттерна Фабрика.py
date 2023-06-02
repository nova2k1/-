class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        self.users.remove(user)


class UserPrinter:
    def print_users(self, users: list):
        for user in users:
            print(user.get_name())