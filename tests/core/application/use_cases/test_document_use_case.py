import pytest
from uuid import UUID
from unittest.mock import Mock, patch
from core.domain.entities.document import Document
from core.application.use_cases.document_use_case import DocumentUseCase

@pytest.fixture
def mock_repository():
    return Mock()

@pytest.fixture
def mock_embedding_service():
    return Mock()

@pytest.fixture
def document_use_case(mock_repository, mock_embedding_service):
    return DocumentUseCase(mock_repository, mock_embedding_service)

def test_save_document(document_use_case, mock_repository, mock_embedding_service):
    # Arrange
    nome = "test.md"
    conteudo = "Teste de conteúdo"
    projeto = "teste"
    embedding = [0.1, 0.2, 0.3]
    
    mock_embedding_service.generate_embedding.return_value = embedding
    
    # Act
    document_use_case.save_document(nome, conteudo, projeto)
    
    # Assert
    mock_embedding_service.generate_embedding.assert_called_once_with(conteudo)
    mock_repository.save.assert_called_once()
    
    # Verifica se o documento salvo tem os dados corretos
    saved_document = mock_repository.save.call_args[0][0]
    assert isinstance(saved_document, Document)
    assert saved_document.nome == nome
    assert saved_document.conteudo == conteudo
    assert saved_document.projeto == projeto
    assert saved_document.embedding == embedding
    assert isinstance(saved_document.id, UUID)

def test_find_similar_documents(document_use_case, mock_repository):
    # Arrange
    query = "consulta teste"
    k = 2
    expected_docs = [
        Document(
            id=UUID("00000000-0000-0000-0000-000000000001"),
            nome="doc1.md",
            conteudo="Conteúdo 1",
            projeto="teste"
        ),
        Document(
            id=UUID("00000000-0000-0000-0000-000000000002"),
            nome="doc2.md",
            conteudo="Conteúdo 2",
            projeto="teste"
        )
    ]
    mock_repository.find_similar.return_value = expected_docs
    
    # Act
    result = document_use_case.find_similar_documents(query, k)
    
    # Assert
    mock_repository.find_similar.assert_called_once_with(query, k)
    assert result == expected_docs 