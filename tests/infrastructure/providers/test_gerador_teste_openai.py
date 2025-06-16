import pytest
from unittest.mock import Mock, patch
from core.entities.historia_usuario import HistoriaUsuario
from infrastructure.providers.gerador_teste_openai import GeradorTesteOpenAI, ContextRetriever
from shared.models.teste_models import TesteGeradoOutput


class MockVectorService:
    def buscar_contexto(self, consulta: str, k: int = 3):
        return [
            "O sistema permite login via Google OAuth 2.0",
            "Validação de email corporativo é obrigatória",
            "Sessão expira em 24 horas"
        ]


class TestContextRetriever:
    def test_retrieve_context_com_vector_service(self):
        # Arrange
        mock_vector = MockVectorService()
        retriever = ContextRetriever(mock_vector)
        historia = HistoriaUsuario("Login Google", "Como usuário desejo fazer login com Google")
        
        # Act
        contexto = retriever.retrieve_context(historia)
        
        # Assert
        assert "Google OAuth 2.0" in contexto
        assert "email corporativo" in contexto
        assert len(contexto) > 0

    def test_retrieve_context_sem_vector_service(self):
        # Arrange
        retriever = ContextRetriever(None)
        historia = HistoriaUsuario("Login Google", "Como usuário desejo fazer login com Google")
        
        # Act
        contexto = retriever.retrieve_context(historia)
        
        # Assert
        assert contexto == ""

    def test_retrieve_context_com_erro_no_vector_service(self):
        # Arrange
        mock_vector = Mock()
        mock_vector.buscar_contexto.side_effect = Exception("Erro de conexão")
        retriever = ContextRetriever(mock_vector)
        historia = HistoriaUsuario("Login Google", "Como usuário desejo fazer login com Google")
        
        # Act
        contexto = retriever.retrieve_context(historia)
        
        # Assert
        assert contexto == ""  # Deve retornar string vazia em caso de erro


class TestGeradorTesteOpenAI:
    @patch('infrastructure.providers.gerador_teste_openai.OpenAI')
    def test_gerar_teste_com_contexto_rag(self, mock_openai_class):
        # Arrange
        mock_client = Mock()
        mock_openai_class.return_value = mock_client
        
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = (
            "Dado que o usuário possui conta Google válida\n"
            "Quando ele clica em 'Login com Google'\n"
            "Então o sistema autentica e redireciona para dashboard"
        )
        mock_client.chat.completions.create.return_value = mock_response
        
        mock_vector = MockVectorService()
        
        with patch('shared.config.env.OpenAIConfig.get_api_key', return_value='fake-key'), \
             patch('shared.config.env.OpenAIConfig.get_model', return_value='gpt-4'), \
             patch('shared.config.env.OpenAIConfig.get_temperature', return_value=0.3):
            
            gerador = GeradorTesteOpenAI(vector_service=mock_vector)
            historia = HistoriaUsuario("Login Google", "Como usuário desejo fazer login com Google")
            
            # Act
            resultado = gerador.gerar_teste(historia)
            
            # Assert
            assert isinstance(resultado, TesteGeradoOutput)
            assert "Google" in resultado.resumo
            assert len(resultado.cenarios_bdd) == 3
            
            # Verificar se o prompt incluiu contexto
            call_args = mock_client.chat.completions.create.call_args
            prompt_enviado = call_args[1]['messages'][1]['content']
            assert "[DOCUMENTAÇÃO DO SISTEMA]" in prompt_enviado
            assert "Google OAuth 2.0" in prompt_enviado 