from sqlalchemy import insert
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler

class UsersRepository:
    async def insert_users(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()