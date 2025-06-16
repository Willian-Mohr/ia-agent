from abc import ABC, abstractmethod
from typing import List
from core.domain.entities.document import Document

class VectorRepository(ABC):
    @abstractmethod
    def save(self, document: Document) -> None:
        """Salva um documento com seu embedding no repositório"""
        pass

    @abstractmethod
    def find_similar(self, query: str, k: int = 3) -> List[Document]:
        """Busca documentos similares à consulta"""
        pass 