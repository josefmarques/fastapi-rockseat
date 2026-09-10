import pytest
from sqlalchemy import text
from .database_connection_handler import DBConnectionHandler

@pytest.mark.asyncio
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        assert db_handler.session is not None

# Força o envio de um comando real para o PostgreSQL
        resultado = await db_handler.session.execute(text("SELECT 1"))
        
        # Confirma se o banco processou e respondeu corretamente
        assert resultado.scalar() == 1