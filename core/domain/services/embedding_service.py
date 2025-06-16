from abc import ABC, abstractmethod
from typing import List

class EmbeddingService(ABC):
    @abstractmethod
    def generate_embedding(self, text: str) -> List[float]:
        """Gera um embedding para o texto fornecido"""
        pass 