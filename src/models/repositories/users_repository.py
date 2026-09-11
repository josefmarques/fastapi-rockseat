# pylint: disable=w0212
from sqlalchemy import insert, select, update, delete
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
            result = await db.session.execute(query) #Executa a consulta SQL montada, buscando todos os registros na tabela Users onde o campo user_name corresponde ao valor fornecido. O await indica que a função deve aguardar a conclusão da operação antes de prosseguir.
            rows = result.fetchall() #Recupera todas as linhas retornadas pela consulta. Cada linha é representada como um objeto Row, que permite acessar os valores das colunas por nome.

            users_list = [dict(row._mapping) for row in rows]
            return users_list #Retorna a lista de dicionários, onde cada dicionário representa um usuário encontrado na consulta. Cada chave do dicionário corresponde ao nome da coluna na tabela Users, e o valor associado é o dado armazenado naquela coluna para o usuário específico.

    async def update_user_by_name(self, user_name:str, update_infos: dict) -> None: # Define o método como assíncrono, recebendo o nome de quem será atualizado e um dicionário com os novos dados.
        async with DBConnectionHandler() as db: # Abre uma sessão segura com o banco de dados.
            query = (
                update(Users) # Inicia a construção de uma instrução SQL de atualização na tabela Users.
                .where(Users.c.user_name == user_name) #
                .values(**update_infos) # Desempacota o dicionário update_infos, aplicando os novos valores nas colunas correspondentes.
            )
            await db.session.execute(query) # Executa a instrução SQL de atualização.
            await db.session.commit() # Confirma a transação, garantindo que as alterações sejam salvas no banco de dados.


    async def delete_users_by_name(self, user_name: str) -> None: # Define o método como assíncrono, recebendo o nome do usuário que será deletado.
        async with DBConnectionHandler() as db: # Abre a sessão segura com o banco de dados.
            query = (
                delete(Users) # Inicializa a construção da instrução SQL de DELETE na tabela Users.
                .where(Users.c.user_name == user_name) # Define a condição (WHERE) estrita para deletar apenas o registro correspondente.
            )
            await db.session.execute(query) # Dispara o comando de deleção para o banco.
            await db.session.commit() # Efetiva a exclusão no banco de dados gravando a transação.