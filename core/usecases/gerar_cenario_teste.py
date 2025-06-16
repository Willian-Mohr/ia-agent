from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.ports.gerador_teste_port import GeradorTestePort
from core.domain.exceptions import GeradorTesteException
from shared.models.teste_models import TesteGeradoOutput


class GerarCenarioTesteUseCase:
    def __init__(self, gerador_teste: GeradorTestePort):
        self._gerador_teste = gerador_teste
        
    def execute(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        """
        Executa a geração de cenários de teste para uma história de usuário
        
        Args:
            historia: História de usuário válida
            
        Returns:
            TesteGeradoOutput: Resultado com cenários gerados
            
        Raises:
            GeradorTesteException: Quando há erro na geração
        """
        if not historia:
            raise GeradorTesteException("História de usuário não pode ser nula")
            
        try:
            resultado = self._gerador_teste.gerar_teste(historia)
            
            # Validação do resultado
            if not resultado.cenarios_bdd or len(resultado.cenarios_bdd) == 0:
                raise GeradorTesteException("Nenhum cenário foi gerado")
                
            return resultado
            
        except Exception as e:
            if isinstance(e, GeradorTesteException):
                raise
            raise GeradorTesteException(f"Erro inesperado na geração de teste: {e}")