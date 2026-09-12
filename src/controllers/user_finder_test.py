import pytest
from .user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.get_users_by_name_att = {}

    async def get_users_by_name(self, user_name: str) -> list[dict]:
        self.get_users_by_name_att["user_name"] = user_name
        return [{ "user_name": "Ola" }, { "user_name": "mundo" }]

@pytest.mark.asyncio
async def test_find_user_by_name():
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    user_name = "Aroldo"

    response = await user_finder.find_user_by_name(user_name) 

    assert user_repo.get_users_by_name_att["user_name"] == user_name

    assert response["type"] == "USERS"
    assert response ["count"] == 2
    assert "atributtes" in response
    assert isinstance(response["atributtes"], list)
    assert isinstance(response["atributtes"][0], dict)