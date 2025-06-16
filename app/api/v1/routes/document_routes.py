from fastapi import APIRouter, Depends
from core.config.database import db_config
from infrastructure.repositories.pgvector_repository import PGVectorRepository
from infrastructure.services.openai_embedding_service import OpenAIEmbeddingService
from core.application.use_cases.document_use_case import DocumentUseCase
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/documentos", tags=["documentos"])

class DocumentInput(BaseModel):
    nome: str
    conteudo: str
    projeto: Optional[str] = None

class DocumentResponse(BaseModel):
    id: str
    nome: str
    conteudo: str
    projeto: Optional[str] = None

def get_document_use_case():
    repository = PGVectorRepository(db_config.connection_string)
    embedding_service = OpenAIEmbeddingService()
    return DocumentUseCase(repository, embedding_service)

@router.post("/", response_model=DocumentResponse)
def criar_documento(
    documento: DocumentInput,
    document_use_case: DocumentUseCase = Depends(get_document_use_case)
):
    doc = document_use_case.save_document(
        nome=documento.nome,
        conteudo=documento.conteudo,
        projeto=documento.projeto
    )
    return DocumentResponse(
        id=str(doc.id),
        nome=doc.nome,
        conteudo=doc.conteudo,
        projeto=doc.projeto
    )

@router.get("/buscar", response_model=List[DocumentResponse])
def buscar_documentos(
    query: str,
    limit: int = 5,
    document_use_case: DocumentUseCase = Depends(get_document_use_case)
):
    documentos = document_use_case.find_similar_documents(query, limit)
    return [
        DocumentResponse(
            id=str(doc.id),
            nome=doc.nome,
            conteudo=doc.conteudo,
            projeto=doc.projeto
        )
        for doc in documentos
    ] 