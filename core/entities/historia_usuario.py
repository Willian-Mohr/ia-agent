from core.domain.exceptions import HistoriaUsuarioInvalidaException


class HistoriaUsuario:
    def __init__(self, titulo: str, descricao: str):
        self._titulo = self._validar_titulo(titulo)
        self._descricao = self._validar_descricao(descricao)

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def descricao(self) -> str:
        return self._descricao
    
    def _validar_titulo(self, titulo: str) -> str:
        if not titulo or len(titulo.strip()) < 5:
            raise HistoriaUsuarioInvalidaException("Título deve ter pelo menos 5 caracteres")
        return titulo.strip()
    
    def _validar_descricao(self, descricao: str) -> str:
        if not descricao or len(descricao.strip()) < 10:
            raise HistoriaUsuarioInvalidaException("Descrição deve ter pelo menos 10 caracteres")
        return descricao.strip()

    def resumo(self) -> str:
        return f"Teste gerado para: {self._titulo}"