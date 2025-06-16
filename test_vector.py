from infrastructure.vectorstore.vector_db import VectorStoreService

vector = VectorStoreService()

# Inserir texto
vector.inserir_documento("login.md", "Como usuário, desejo autenticar com Google.")

# Buscar
resultados = vector.buscar_contexto("autenticação")
print(resultados)
