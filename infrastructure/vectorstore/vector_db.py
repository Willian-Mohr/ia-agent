import os
import uuid
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

CONNECTION_STRING = "postgresql+psycopg2://iauser:secret@localhost:5432/iadb"

class VectorStoreService:
    def __init__(self):
        self.store = PGVector(
            collection_name="documentos",
            connection_string=CONNECTION_STRING,
            embedding_function=OpenAIEmbeddings()
        )

    def inserir_documento(self, nome: str, texto: str, projeto: str = "default"):
        doc = Document(page_content=texto, metadata={"nome": nome, "projeto": projeto, "id": str(uuid.uuid4())})
        self.store.add_documents([doc])

    def buscar_contexto(self, consulta: str, k: int = 3):
        docs = self.store.similarity_search(query=consulta, k=k)
        return [doc.page_content for doc in docs]
