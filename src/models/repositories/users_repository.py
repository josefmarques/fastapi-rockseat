from sqlalchemy import insert, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler


class UsersRepository:
    async def insert_users(self, user_infos: dict) -> None: #Define o método como assíncrono, permitindo que a aplicação atenda outras requisições enquanto aguarda a resposta do banco de dados.
        async with DBConnectionHandler() as db: #Aciona o gerenciador de contexto criado no passo anterior. Ele abre uma conexão segura com o PostgreSQL (__aenter__) e garante que ela será fechada automaticamente ao final do bloco (__aexit__), prevenindo vazamentos de memória.
            query = insert(Users).values(**user_infos) #Constrói a instrução SQL de inserção. O operador ** desempacota o dicionário user_infos, extraindo as chaves (ex: user_name, age) e inserindo seus respectivos valores diretamente nas colunas correspondentes da tabela.
            await db.session.execute(query) #Dispara o comando SQL montado para o banco de dados. O await sinaliza que o Python deve pausar essa função específica até o PostgreSQL terminar o processamento.
            await db.session.commit() #Confirma a transação. O banco de dados só grava a informação definitivamente no disco após receber o comando de commit. Sem essa linha, a inserção seria revertida automaticamente ao encerrar a sessão.

    async def get_users_by_name(self, user_name: str) -> list[dict]: #Define o método como assíncrono e especifica que ele retornará uma lista de objetos do tipo Users.
        async with DBConnectionHandler() as db: #Abre uma sessão segura com o banco de dados, garantindo que ela será fechada automaticamente ao final do bloco.
            query = (
                select(Users)
                .where(Users.c.user_name == user_name)
            )
            result = await query.all() #Executa a consulta e aguarda o resultado. O método all() retorna todos os registros que atendem à condição especificada.
            return result #Retorna a lista de usuários encontrados para o chamador da função.





