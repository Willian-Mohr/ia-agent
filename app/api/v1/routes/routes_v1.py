from fastapi import APIRouter

router = APIRouter()

@router.get("/status", tags=["status"])
def status():
    return {"status": "ok", "mensagem": "IA Agent iniciado com sucesso"}
