from infrastructure.vectorstore.vector_db import VectorStoreService

vector = VectorStoreService()

# Inserir texto
vector.inserir_documento("login-google.md", "Como usuário, desejo autenticar com Google.")
vector.inserir_documento("login-facebook.md", "Como usuário, desejo autenticar com Facebook.")

# Buscar
resultados = vector.buscar_contexto("autenticação")
print(resultados)
