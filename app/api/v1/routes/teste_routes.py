from fastapi import APIRouter
from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.gerar_cenario_teste import GerarCenarioTesteUseCase
from infrastructure.providers.gerador_teste_fake import GeradorTesteFake
from shared.models.teste_models import HistoriaUsuarioInput
from infrastructure.providers.gerador_teste_openai import GeradorTesteOpenAI

router = APIRouter(prefix="/testes", tags=["testes"])

@router.post("/gerar")
def gerar_teste(historia_input: HistoriaUsuarioInput):
    historia = HistoriaUsuario(
        titulo=historia_input.titulo,
        descricao=historia_input.descricao
    )
    
    gerador_openai = GeradorTesteOpenAI()
    usecase = GerarCenarioTesteUseCase(gerador_openai)
    return usecase.execute(historia)