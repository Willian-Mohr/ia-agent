from core.usecases.gerar_cenario_teste import GerarCenarioTesteUseCase
from core.usecases.ports.gerador_teste_port import GeradorTestePort
from infrastructure.providers.gerador_teste_openai import GeradorTesteOpenAI
from infrastructure.vectorstore.vector_db import VectorStoreService


class DependencyFactory:
    """Factory para criar e injetar dependências seguindo o princípio DIP"""
    
    @staticmethod
    def create_vector_store_service() -> VectorStoreService:
        """Cria uma instância do serviço de vectorstore com threshold mais restritivo"""
        return VectorStoreService(similarity_threshold=0.85)
    
    @staticmethod
    def create_gerador_teste_port() -> GeradorTestePort:
        """Cria uma instância do adaptador de geração de teste com RAG"""
        vector_service = DependencyFactory.create_vector_store_service()
        return GeradorTesteOpenAI(vector_service=vector_service)
    
    @staticmethod
    def create_gerar_cenario_teste_usecase() -> GerarCenarioTesteUseCase:
        """Cria uma instância do caso de uso com suas dependências injetadas"""
        gerador_teste = DependencyFactory.create_gerador_teste_port()
        return GerarCenarioTesteUseCase(gerador_teste) 