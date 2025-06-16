from fastapi import FastAPI
from app.api.v1.routes import routes_v1, teste_routes, documentos_routes

def create_app() -> FastAPI:
    app = FastAPI(title="IA Agent")
    app.include_router(routes_v1.router, prefix="/api/v1")
    app.include_router(teste_routes.router, prefix="/api/v1")
    app.include_router(documentos_routes.router, prefix="/api/v1")
    return app

app = create_app()
