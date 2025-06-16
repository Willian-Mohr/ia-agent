from typing import List
from langchain_openai import OpenAIEmbeddings
from core.domain.services.embedding_service import EmbeddingService

class OpenAIEmbeddingService(EmbeddingService):
    def __init__(self):
        self._embeddings = OpenAIEmbeddings()

    def generate_embedding(self, text: str) -> List[float]:
        """Gera um embedding para o texto usando OpenAI"""
        return self._embeddings.embed_query(text) 