from src.models.repositories.users_repository import UsersRepositoryInterface

class UserRegister:
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.users_repository = users_repository