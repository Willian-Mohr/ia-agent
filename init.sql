CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documentos (
    id UUID PRIMARY KEY,
    projeto TEXT,
    nome TEXT,
    conteudo TEXT,
    embedding vector(1536)
);