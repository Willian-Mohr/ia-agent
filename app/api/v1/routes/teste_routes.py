from fastapi import APIRouter
from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.gerar_cenario_teste import GerarCenarioTesteUseCase
from shared.models.teste_models import HistoriaUsuarioInput

router = APIRouter(prefix="/testes", tags=["testes"])

@router.post("/gerar")
def gerar_teste(historia_input: HistoriaUsuarioInput):
    historia = HistoriaUsuario(
        titulo=historia_input.titulo,
        descricao=historia_input.descricao
        )
    usecase = GerarCenarioTesteUseCase()
    return usecase.execute(historia)