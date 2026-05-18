# pylint:disable = E1101
import pytest
from .users_repository import UsersRepository


@pytest.mark.asyncio
#@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {
        "user_name": "Ana Maria",
        "age": 60,
        "uf": "BA"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.skip(reason="Select in DB")
@pytest.mark.asyncio
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("NomeDeTeste")
    print(response)


@pytest.mark.skip(reason="Update in DB")
@pytest.mark.asyncio
async def test_update_user():
    updated_data = {
        "age": 100,
        "uf": "RJ"
    }

    repo = UsersRepository()
    await repo.update_user("NomeDeTeste", updated_data)

    # Verifica se a atualização foi aplicada
    response = await repo.get_users_by_name("NomeDeTeste")
    print(response)


@pytest.mark.skip(reason="Delete in DB")
@pytest.mark.asyncio
async def test_delete_user():
    repo = UsersRepository()
    await repo.delete_user("Jose Marques")

    # Verifica se foi removido (deve retornar lista vazia)
    response = await repo.get_users_by_name("Jose Marques")
    print(response)
