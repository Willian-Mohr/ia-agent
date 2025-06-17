from fastapi import APIRouter, HTTPException, status, Query
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
def buscar_documentos(
    query: str, 
    limit: int = Query(default=3, ge=1, le=10, description="Número máximo de documentos")
):
    """Busca documentos por similaridade semântica com threshold de qualidade"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        resultados = vector_service.buscar_contexto(consulta=query, k=limit)
        
        return {
            "query": query,
            "total_encontrados": len(resultados),
            "documentos": resultados,
            "threshold_usado": vector_service.similarity_threshold
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca: {str(e)}"
        )

@router.get("/debug/buscar-com-scores/{query}")
def buscar_documentos_com_scores(
    query: str, 
    limit: int = Query(default=3, ge=1, le=10)
):
    """Busca documentos retornando scores de similaridade para debug"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        resultados = vector_service.buscar_contexto_com_scores(consulta=query, k=limit)
        
        documentos_formatados = [
            {
                "conteudo": doc,
                "similarity_score": round(score, 3),
                "relevante": score >= vector_service.similarity_threshold
            }
            for doc, score in resultados
        ]
        
        return {
            "query": query,
            "threshold_configurado": vector_service.similarity_threshold,
            "total_encontrados": len(documentos_formatados),
            "documentos": documentos_formatados
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro na busca com scores: {str(e)}"
        )

@router.get("/debug/listar-todos")
def listar_todos_documentos():
    """Lista todos os documentos armazenados para administração"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        documentos = vector_service.listar_todos_documentos()
        
        return {
            "total_documentos": len(documentos),
            "documentos": documentos
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar documentos: {str(e)}"
        )

@router.delete("/debug/limpar-testes")
def remover_documentos_teste():
    """Remove documentos de teste da base de dados"""
    try:
        vector_service = DependencyFactory.create_vector_store_service()
        removidos = vector_service.remover_documentos_teste()
        
        return {
            "status": "Limpeza concluída",
            "documentos_removidos": removidos,
            "mensagem": f"Foram removidos {removidos} documentos de teste"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao remover documentos teste: {str(e)}"
        ) 