from sqlalchemy import insert
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler

class UsersRepository:
    async def insert_users(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

# Funcionamento de cada linha:

#     class UsersRepository:: Nome da classe corrigido com a letra "y" no final, seguindo o padrão correto de nomenclatura.

#     async def insert_users(...): Define o método como assíncrono, permitindo que a aplicação atenda outras requisições enquanto aguarda a resposta do banco de dados.

#     async with DBConnectionHandler() as db:: Aciona o gerenciador de contexto criado no passo anterior. Ele abre uma conexão segura com o PostgreSQL (__aenter__) e garante que ela será fechada automaticamente ao final do bloco (__aexit__), prevenindo vazamentos de memória.

#     insert(Users).values(**user_infos): Constrói a instrução SQL de inserção. O operador ** desempacota o dicionário user_infos, extraindo as chaves (ex: user_name, age) e inserindo seus respectivos valores diretamente nas colunas correspondentes da tabela.

#     await db.session.execute(query): Dispara o comando SQL montado para o banco de dados. O await sinaliza que o Python deve pausar essa função específica até o PostgreSQL terminar o processamento.

#     await db.session.commit(): Confirma a transação. O banco de dados só grava a informação definitivamente no disco após receber o comando de commit. Sem essa linha, a inserção seria revertida automaticamente ao encerrar a sessão.