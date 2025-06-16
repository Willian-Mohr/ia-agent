from typing import List
from langchain_community.vectorstores import PGVector
from langchain_core.documents import Document as LangchainDocument
from core.domain.entities.document import Document
from core.domain.repositories.vector_repository import VectorRepository

class PGVectorRepository(VectorRepository):
    def __init__(self, connection_string: str, collection_name: str = "documentos"):
        self._store = PGVector(
            collection_name=collection_name,
            connection_string=connection_string
        )

    def save(self, document: Document) -> None:
        """Salva um documento com seu embedding no PostgreSQL"""
        langchain_doc = LangchainDocument(
            page_content=document.conteudo,
            metadata={
                "id": str(document.id),
                "nome": document.nome,
                "projeto": document.projeto
            }
        )
        self._store.add_documents([langchain_doc])

    def find_similar(self, query: str, k: int = 3) -> List[Document]:
        """Busca documentos similares à consulta"""
        docs = self._store.similarity_search(query=query, k=k)
        return [
            Document(
                id=doc.metadata["id"],
                nome=doc.metadata["nome"],
                conteudo=doc.page_content,
                projeto=doc.metadata["projeto"]
            )
            for doc in docs
        ] 