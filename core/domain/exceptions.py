class DomainException(Exception):
    """Exceção base para erros de domínio"""
    pass


class HistoriaUsuarioInvalidaException(DomainException):
    """Exceção para história de usuário inválida"""
    pass


class GeradorTesteException(DomainException):
    """Exceção para erros na geração de testes"""
    pass


class ConfiguracaoInvalidaException(DomainException):
    """Exceção para configurações inválidas"""
    pass 