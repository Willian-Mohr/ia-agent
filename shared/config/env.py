import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class EnvConfig:
    """Responsável por gerenciar configurações de ambiente com validação"""
    
    @staticmethod
    def _get_required_env(key: str) -> str:
        """Obtém variável obrigatória do ambiente com validação"""
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Variável de ambiente obrigatória não encontrada: {key}")
        return value
    
    @staticmethod
    def _get_optional_env(key: str, default: str) -> str:
        """Obtém variável opcional do ambiente com valor padrão"""
        return os.getenv(key, default)


class OpenAIConfig:
    """Configurações específicas para OpenAI"""
    
    @staticmethod
    def get_api_key() -> str:
        return EnvConfig._get_required_env("OPENAI_API_KEY")
    
    @staticmethod
    def get_model() -> str:
        return EnvConfig._get_optional_env("OPENAI_MODEL", "gpt-4")
    
    @staticmethod
    def get_temperature() -> float:
        temp_str = EnvConfig._get_optional_env("OPENAI_TEMPERATURE", "0.3")
        try:
            return float(temp_str)
        except ValueError:
            return 0.3

OPENAI_API_KEY = OpenAIConfig.get_api_key()