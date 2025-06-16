from fastapi import APIRouter, HTTPException, status
from core.application.factories import DependencyFactory
from shared.models.documento_models import DocumentoInput, DocumentoOutput
from typing import List

router = APIRouter(prefix="/documentos", tags=["documentos"])

@router.post("/upload", response_model=DocumentoOutput)
def upload_documento(documento_input: DocumentoInput):
    """Upload de documento para enriquecer o contexto do agente IA"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        
        vector_service.inserir_documento(
            nome=documento_input.nome,
            texto=documento_input.conteudo,
            projeto=documento_input.projeto
        )
        
        return DocumentoOutput(
            nome=documento_input.nome,
            projeto=documento_input.projeto,
            status="Documento inserido com sucesso",
            total_caracteres=len(documento_input.conteudo)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao inserir documento: {str(e)}"
        )

@router.get("/buscar/{query}")
def buscar_documentos(query: str, limit: int = 3):
    """Busca documentos por similaridade semântica"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        resultados = vector_service.buscar_contexto(consulta=query, k=limit)
        
        return {
            "query": query,
            "total_encontrados": len(resultados),
            "documentos": resultados
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca: {str(e)}"
        ) 