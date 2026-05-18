from abc import ABC, abstractmethod


class UsersRepositoryInterface(ABC):
    
    @abstractmethod
    async def insert_users(self, users_infos: dict) -> None: pass
    
    @abstractmethod
    async def get_users_by_name(self, user_name: str) -> list[dict]: pass
    
    