from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuários do sistema"])

@users_routes.post ("/users")
async def criar_usuario():
    return JSONResponse(content={"message": "Hello, World!"}, status_code=201)