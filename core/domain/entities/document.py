from dataclasses import dataclass
from uuid import UUID
from typing import Optional

@dataclass
class Document:
    id: UUID
    nome: str
    conteudo: str
    projeto: str
    embedding: Optional[list[float]] = None 