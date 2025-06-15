from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.ports.gerador_teste_port import GeradorTestePort
from shared.models.teste_models import TesteGeradoOutput

class GerarCenarioTesteUseCase:
    def __init__(self, gerador_teste: GeradorTestePort):
        self.gerador_teste = gerador_teste
        
    def execute(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        return self.gerador_teste.gerar_teste(historia)