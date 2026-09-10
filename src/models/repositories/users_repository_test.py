import pytest
from .users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason="Este teste é apenas um exemplo e não deve ser executado em produção.")
async def test_insert_users():
    new_user = {
        "user_name": "NomeDeTeste",
        "age": 99,
        "uf": "SP"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)