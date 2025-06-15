import pytest
from core.entities.historia_usuario import HistoriaUsuario
from infrastructure.providers.gerador_teste_fake import GeradorTesteFake

def test_gerar_teste_deve_retornar_cenario_formatado():
    # Arrange
    historia = HistoriaUsuario("Login Google", "Desejo me autenticar via Google")
    gerador = GeradorTesteFake()
    
    # Act
    resultado = gerador.gerar_teste(historia)
    
    # Assert
    assert resultado.resumo == "Teste gerado para: Login Google"
    assert len(resultado.cenarios_bdd) == 3
    assert resultado.cenarios_bdd[0] == "Dado que Desejo me autenticar via Google"
    assert resultado.cenarios_bdd[1] == "Quando o usuário interage com a funcionalidade"
    assert resultado.cenarios_bdd[2] == "Então o sistema responde corretamente" 