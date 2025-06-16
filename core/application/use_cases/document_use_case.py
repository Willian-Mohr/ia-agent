from uuid import uuid4
from typing import List
from core.domain.entities.document import Document
from core.domain.repositories.vector_repository import VectorRepository
from core.domain.services.embedding_service import EmbeddingService

class DocumentUseCase:
    def __init__(
        self,
        vector_repository: VectorRepository,
        embedding_service: EmbeddingService
    ):
        self._vector_repository = vector_repository
        self._embedding_service = embedding_service

    def save_document(self, nome: str, conteudo: str, projeto: str = "default") -> None:
        """Salva um novo documento com seu embedding"""
        embedding = self._embedding_service.generate_embedding(conteudo)
        document = Document(
            id=uuid4(),
            nome=nome,
            conteudo=conteudo,
            projeto=projeto,
            embedding=embedding
        )
        self._vector_repository.save(document)

    def find_similar_documents(self, query: str, k: int = 3) -> List[Document]:
        """Busca documentos similares à consulta"""
        return self._vector_repository.find_similar(query, k) 