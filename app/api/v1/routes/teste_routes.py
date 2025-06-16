from fastapi import APIRouter, HTTPException, status
from core.entities.historia_usuario import HistoriaUsuario
from core.application.factories import DependencyFactory
from core.domain.exceptions import (
    HistoriaUsuarioInvalidaException, 
    GeradorTesteException, 
    ConfiguracaoInvalidaException
)
from shared.models.teste_models import HistoriaUsuarioInput

router = APIRouter(prefix="/testes", tags=["testes"])

@router.post("/gerar")
def gerar_teste(historia_input: HistoriaUsuarioInput):
    try:
        historia = HistoriaUsuario(
            titulo=historia_input.titulo,
            descricao=historia_input.descricao
        )
        
        usecase = DependencyFactory.create_gerar_cenario_teste_usecase()
        return usecase.execute(historia)
        
    except HistoriaUsuarioInvalidaException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"História de usuário inválida: {str(e)}"
        )
    except GeradorTesteException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na geração de teste: {str(e)}"
        )
    except ConfiguracaoInvalidaException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro de configuração: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno do servidor"
        )