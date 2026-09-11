from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    async def insert_users(self, user_infos: dict) -> None: pass

    @abstractmethod
    async def get_users_by_name(self, user_name: str) -> list[dict]: pass

    @abstractmethod
    async def update_user_by_name(self, user_name:str, update_infos: dict) -> None: pass

    @abstractmethod
    async def delete_users_by_name(self, user_name: str) -> None: pass
     