# pylint:disable = W0212
from sqlalchemy import delete, insert, select, update
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler
from .interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    async def insert_users(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

    async def get_users_by_name(self, user_name: str) -> list[dict]:
        async with DBConnectionHandler() as db:
            query = (
                select(Users)
                .where(Users.c.user_name == user_name)
            )
            result = await db.session.execute(query)
            rows = result.fetchall()
            users_list = [dict(row._mapping) for row in rows]
            return users_list

    async def update_user(self, user_name: str, updated_data: dict) -> None:
        async with DBConnectionHandler() as db:
            query = (
                update(Users)
                .where(Users.c.user_name == user_name)
                .values(**updated_data)
            )
            await db.session.execute(query)
            await db.session.commit()

    async def delete_user(self, user_name: str) -> None:
        async with DBConnectionHandler() as db:
            query = (
                delete(Users)
                .where(Users.c.user_name == user_name)
            )
            await db.session.execute(query)
            await db.session.commit()
