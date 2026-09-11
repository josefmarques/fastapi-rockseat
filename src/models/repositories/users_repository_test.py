import pytest
from .users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB.")
async def test_insert_users():
    new_user = {
        "user_name": "Ana Marques",
        "age": 69,
        "uf": "BA"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Select in DB.")
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("NomeDeTeste")
    print(response)  # Adicione esta linha para depuração

@pytest.mark.asyncio
#@pytest.mark.skip(reason="Update in DB.")
async def test_update_users():
    update_data = {
        "user_name": "Murilo César",
        "age": 79,
        "uf": "MG"  
    }
    repo = UsersRepository()
    # Chama a função passando o nome do usuário e o dicionário com os dados novos
    await repo.update_user_by_name("Murilo César", update_data)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Delete in DB.")
async def test_delete_users():
    repo = UsersRepository()
    # Chama a função passando apenas o nome do usuário a ser deletado
    await repo.delete_users_by_name("NomeDeTeste")