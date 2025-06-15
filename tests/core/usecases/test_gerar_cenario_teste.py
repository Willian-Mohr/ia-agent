import pytest
from core.entities.historia_usuario import HistoriaUsuario
from core.usecases.gerar_cenario_teste import GerarCenarioTesteUseCase
from core.usecases.ports.gerador_teste_port import GeradorTestePort
from shared.models.teste_models import TesteGeradoOutput

class GeradorTesteMock(GeradorTestePort):
    def gerar_teste(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        return TesteGeradoOutput(
            resumo="Simulado",
            cenarios_bdd=["Dado fake", "Quando fake", "Então fake"]
        )

def test_execute_deve_gerar_cenario_com_sucesso():
    # Arrange
    historia = HistoriaUsuario("Login Google", "Desejo me autenticar via Google")
    gerador_mock = GeradorTesteMock()
    usecase = GerarCenarioTesteUseCase(gerador_mock)
    
    # Act
    resultado = usecase.execute(historia)
    
    # Assert
    assert resultado.resumo == "Simulado"
    assert len(resultado.cenarios_bdd) == 3
    assert resultado.cenarios_bdd[0].startswith("Dado") 