from pydantic import BaseModel, Field
from typing import List


class HistoriaUsuarioInput(BaseModel):
    titulo: str = Field(..., min_length=5)
    descricao: str = Field(..., min_length=10)
    
class TesteGeradoOutput(BaseModel):
    resumo: str
    cenarios_bdd: List[str]