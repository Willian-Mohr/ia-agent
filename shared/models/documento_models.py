from pydantic import BaseModel, Field
from typing import Optional


class DocumentoInput(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do documento")
    conteudo: str = Field(..., min_length=10, description="Conteúdo do documento")
    projeto: str = Field(default="default", description="Projeto ao qual o documento pertence")


class DocumentoOutput(BaseModel):
    nome: str
    projeto: str
    status: str
    total_caracteres: int 