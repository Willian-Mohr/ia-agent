from abc import ABC, abstractmethod
from core.entities.historia_usuario import HistoriaUsuario
from shared.models.teste_models import TesteGeradoOutput

class GeradorTestePort(ABC):
    @abstractmethod
    def gerar_teste(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        pass