import pytest
from .user_register import UserRegister

class UserRepositoryMock:
    def __init__(self):
        self.insert_users_att = {}

    async def insert_users(self, user_data: dict):
        self.insert_users_att["user_data"] = user_data

@pytest.mark.asyncio
async def test_register_user():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        "user_name": "Maria Silva",
        "age": 32,
        "uf": "MG"
    }

    response = await user_register.register_user(user_data)
    print()
    print(response)

    assert user_repository.insert_users_att["user_data"] == user_data

    assert response["type"] == "USERS"
    assert response["count"] == 1
    assert response["attributes"] == user_data

@pytest.mark.asyncio
async def test_register_user_error_uf():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_uf_user_data = {
        "user_name": "Maria Silva",
        "age": 32,
        "uf": "ES"
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_uf_user_data)