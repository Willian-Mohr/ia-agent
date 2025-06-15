class HistoriaUsuario:
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao

    def resumo(self) -> str:
        return f"Teste gerado para: {self.titulo}"