import os
import uuid
from typing import List, Tuple
from langchain.vectorstores.pgvector import PGVector
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

CONNECTION_STRING = "postgresql+psycopg2://iauser:secret@localhost:5432/iadb"

class VectorStoreService:
    def __init__(self, similarity_threshold: float = 0.7):
        """
        Args:
            similarity_threshold: Limiar de similaridade (0.0 a 1.0). 
                                 Valores mais altos = resultados mais relevantes
        """
        self.store = PGVector(
            collection_name="documentos",
            connection_string=CONNECTION_STRING,
            embedding_function=OpenAIEmbeddings()
        )
        self.similarity_threshold = similarity_threshold

    def inserir_documento(self, nome: str, texto: str, projeto: str = "default"):
        doc = Document(page_content=texto, metadata={"nome": nome, "projeto": projeto, "id": str(uuid.uuid4())})
        self.store.add_documents([doc])

    def buscar_contexto(self, consulta: str, k: int = 3) -> List[str]:
        """
        Busca documentos por similaridade com threshold de qualidade
        
        Args:
            consulta: Termo de busca
            k: Número máximo de documentos
            
        Returns:
            Lista de documentos relevantes (filtrados por similaridade)
        """
        try:
            # Busca com score de similaridade
            docs_with_scores = self.store.similarity_search_with_score(
                query=consulta, 
                k=k * 2  # Busca mais documentos para filtrar depois
            )
            
            # Filtrar por threshold de similaridade
            # Nota: pgvector retorna distância (menor = mais similar)
            # Convertemos para similaridade: similarity = 1 - distance
            documentos_relevantes = []
            
            for doc, distance in docs_with_scores:
                similarity = 1 - distance
                
                if similarity >= self.similarity_threshold:
                    documentos_relevantes.append(doc.page_content)
                    
                # Limitar ao número solicitado
                if len(documentos_relevantes) >= k:
                    break
            
            return documentos_relevantes
            
        except Exception as e:
            # Fallback para busca simples em caso de erro
            docs = self.store.similarity_search(query=consulta, k=k)
            return [doc.page_content for doc in docs]

    def buscar_contexto_com_scores(self, consulta: str, k: int = 3) -> List[Tuple[str, float]]:
        """
        Busca documentos retornando também os scores de similaridade
        Útil para debugging e análise
        """
        try:
            docs_with_scores = self.store.similarity_search_with_score(query=consulta, k=k)
            
            resultados = []
            for doc, distance in docs_with_scores:
                similarity = 1 - distance
                resultados.append((doc.page_content, similarity))
                
            return resultados
            
        except Exception:
            return []

    def listar_todos_documentos(self) -> List[dict]:
        """Lista todos os documentos para debug/administração"""
        try:
            # Busca genérica para pegar todos os documentos
            docs = self.store.similarity_search(query="documento", k=100)
            
            return [
                {
                    "nome": doc.metadata.get("nome", "N/A"),
                    "projeto": doc.metadata.get("projeto", "default"),
                    "conteudo_preview": doc.page_content[:100] + "..." if len(doc.page_content) > 100 else doc.page_content,
                    "conteudo_completo": doc.page_content
                }
                for doc in docs
            ]
        except Exception:
            return []

    def remover_documentos_teste(self) -> int:
        """
        Remove documentos criados para teste (conteúdo curto e genérico)
        Retorna número de documentos removidos
        """
        try:
            import psycopg2
            
            # Conectar diretamente ao PostgreSQL para deletar
            conn = psycopg2.connect(
                host="localhost",
                database="iadb", 
                user="iauser",
                password="secret"
            )
            
            cursor = conn.cursor()
            
            # Remover documentos muito curtos ou com conteúdo de teste
            cursor.execute("""
                DELETE FROM langchain_pg_embedding 
                WHERE document LIKE '%login via Google e verifica e-mail%'
                   OR LENGTH(document) < 50
                   OR document LIKE '%test%'
                   OR document LIKE '%teste%'
            """)
            
            rows_deleted = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            
            return rows_deleted
            
        except Exception as e:
            print(f"Erro ao remover documentos teste: {e}")
            return 0

