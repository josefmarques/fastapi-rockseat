from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# String adaptada para o PostgreSQL utilizando o driver asyncpg
CONNECTION_STRING = "postgresql+asyncpg://zemarques:mrq831028@localhost:5432/estoque-db"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False, # impede que o SQLAlchemy imprima no terminal todos os comandos SQL que estão sendo executados nos bastidores.
    pool_size=2, # não criar mais d
    max_overflow=0, # não permitir conexões extras além do limite de 2
    pool_timeout=30 # tempo máximo de espera para pegar uma conexão do pool antes de gerar um erro
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DBConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = async_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


# O que cada bloco faz detalhadamente:  

#     from typing import Optional: Importa o tipo Optional para avisar ao Python (e ao seu editor) que uma variável pode conter um valor específico ou estar vazia (None).  

#     from sqlalchemy...: Importa as ferramentas necessárias para criar o motor de conexão assíncrono e definir os tipos da sessão.  

#     CONNECTION_STRING = ...: Define a URL exata de onde está o seu banco de dados, utilizando suas credenciais locais do PostgreSQL e exigindo o driver assíncrono asyncpg.

#     engine = create_async_engine(...): Cria o motor principal que vai gerenciar a comunicação física com o banco de dados.

#         echo=False: Impede que o SQLAlchemy imprima no terminal todos os comandos SQL que estão sendo executados nos bastidores.

#         pool_size=2: Mantém até 2 conexões abertas simultaneamente aguardando uso (ótimo para não sobrecarregar o banco).

#         max_overflow=0: Define que o sistema não pode abrir conexões extras além do limite de 2 que foi configurado acima.

#         pool_timeout=30: Se o sistema tentar pegar uma conexão e todas estiverem ocupadas, ele espera até 30 segundos antes de retornar um erro de "timeout".

#     async_session = sessionmaker(...): Cria uma fábrica de sessões. O expire_on_commit=False evita que os objetos consultados percam seus dados logo após você salvar (comitar) algo no banco.

#     class DBConnectionHandler:: Define uma classe que servirá como um "Gerenciador de Contexto" (Context Manager) para abrir e fechar conexões de forma segura.

#     def __init__(self) -> None:: É o método construtor. Ele apenas cria a variável self.session vazia (None) quando a classe é chamada.

#     async def __aenter__(self):: É um método mágico acionado automaticamente quando você usa a instrução async with DBConnectionHandler(). Ele gera uma nova sessão chamando o async_session() e devolve a própria classe pronta para uso.

#     async def __aexit__(self, ...):: É o método mágico acionado automaticamente quando o bloco de código do async with termina (seja com sucesso ou erro). A instrução await self.session.close() garante que a conexão com o banco seja fechada e devolvida ao pool, prevenindo vazamentos de memória e conexões presas.