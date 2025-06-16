# Implementações RAG - IA Agent

## 🚀 Resumo das Implementações

### 1. **RAG (Retrieval-Augmented Generation) Implementado**

#### ✅ Integração com VectorStore
- `ContextRetriever`: Nova classe responsável pela recuperação de contexto
- Integração com `VectorStoreService` existente
- Busca semântica baseada no título e descrição da história

#### ✅ Melhoria no `GeradorTesteOpenAI`
```python
# Antes: Prompt simples
prompt = build_teste_prompt(historia)

# Depois: Prompt enriquecido com contexto
contexto = self._context_retriever.retrieve_context(historia)
prompt = build_teste_prompt(historia, contexto)
```

#### ✅ Separação de Responsabilidades (SRP)
- `PromptBuilder`: Constrói prompts (com/sem contexto)
- `OpenAIResponseProcessor`: Processa respostas da OpenAI 
- `ContextRetriever`: Recupera contexto vetorizado
- `GeradorTesteOpenAI`: Orquestra todo o processo

---

### 2. **Endpoint de Upload de Documentos**

#### ✅ Nova API REST
```http
POST /api/v1/documentos/upload
GET /api/v1/documentos/buscar/{query}
```

#### ✅ DTOs Implementados
- `DocumentoInput`: Validação de entrada
- `DocumentoOutput`: Resposta estruturada

#### ✅ Integração com Factory Pattern
```python
vector_service = DependencyFactory.create_vector_store_service()
```

---

### 3. **Testes Automatizados**

#### ✅ Testes para RAG
- Mock do `VectorStoreService`
- Validação de integração contexto + prompt
- Cenários de erro e fallback

#### ✅ Cobertura de Casos
- Com vectorstore ativo
- Sem vectorstore (graceful degradation)
- Erro na busca vetorial (resilience)

---

## 🏗️ Arquitetura Aplicada

### ✅ Clean Architecture
```
app/               → Interface (FastAPI routes)
core/              → Use cases e entities 
infrastructure/    → Adapters (OpenAI, VectorStore)
shared/            → Models e configurações
```

### ✅ SOLID Principles
- **SRP**: Cada classe tem uma responsabilidade única
- **OCP**: Aberto para extensão (novos provedores de IA)
- **LSP**: Implementações substituíveis via GeradorTestePort
- **ISP**: Interfaces específicas e focadas
- **DIP**: Inversão de dependências via factory

### ✅ Design Patterns
- **Factory Pattern**: `DependencyFactory`
- **Strategy Pattern**: `GeradorTestePort` com múltiplas implementações
- **Builder Pattern**: `PromptBuilder`
- **Adapter Pattern**: `GeradorTesteOpenAI`

---

## 🧪 Como Testar

### 1. Upload de Documento
```bash
curl -X POST "http://localhost:8000/api/v1/documentos/upload" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "specs_login.md",
    "conteudo": "O sistema permite autenticação via Google OAuth 2.0 com validação de email corporativo.",
    "projeto": "auth-system"
  }'
```

### 2. Geração de Teste com Contexto
```bash
curl -X POST "http://localhost:8000/api/v1/testes/gerar" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Login com Google",
    "descricao": "Como usuário, desejo autenticar via Google para acesso rápido"
  }'
```

### 3. Busca de Contexto
```bash
curl "http://localhost:8000/api/v1/documentos/buscar/autenticação?limit=3"
```

---

## 🎯 Comparação Java vs Python

| Conceito Java | Implementação Python |
|---------------|---------------------|
| `@Service` | Classe com injeção manual |
| `@Repository` | `VectorStoreService` |
| `@RestController` | FastAPI `APIRouter` |
| `ResponseEntity<>` | Pydantic models |
| JUnit + Mockito | pytest + unittest.mock |
| Spring Factory | `DependencyFactory` |

---

## ✅ Benefícios Implementados

1. **Contextualização Inteligente**: IA usa documentação existente
2. **Escalabilidade**: Novo contexto via API REST
3. **Testabilidade**: Mocks e isolamento total
4. **Manutenibilidade**: Separação clara de responsabilidades
5. **Extensibilidade**: Fácil adição de novos provedores de IA 