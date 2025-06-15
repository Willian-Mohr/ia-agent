from fastapi import APIRouter
from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.gerar_cenario_teste import GerarCenarioTesteUseCase
from infrastructure.providers.gerador_teste_fake import GeradorTesteFake
from shared.models.teste_models import HistoriaUsuarioInput

router = APIRouter(prefix="/testes", tags=["testes"])

@router.post("/gerar")
def gerar_teste(historia_input: HistoriaUsuarioInput):
    historia = HistoriaUsuario(
        titulo=historia_input.titulo,
        descricao=historia_input.descricao
    )
    gerador_fake = GeradorTesteFake()
    usecase = GerarCenarioTesteUseCase(gerador_fake)
    return usecase.execute(historia)