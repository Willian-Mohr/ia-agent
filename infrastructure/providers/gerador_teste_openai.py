from openai import OpenAI
from typing import List, Optional
from core.usecases.ports.gerador_teste_port import GeradorTestePort
from core.entities.historia_usuario import HistoriaUsuario
from core.domain.exceptions import GeradorTesteException, ConfiguracaoInvalidaException
from shared.models.teste_models import TesteGeradoOutput
from shared.config.env import OpenAIConfig


class PromptBuilder:
    """Responsável por construir prompts para geração de testes"""
    
    @staticmethod
    def build_teste_prompt(historia: HistoriaUsuario, contexto: Optional[str] = None) -> str:
        prompt_base = (
            f"Com base na seguinte história de usuário:\n\n"
            f"Título: {historia.titulo}\n"
            f"Descrição: {historia.descricao}\n\n"
        )
        
        if contexto:
            prompt_base += (
                f"[DOCUMENTAÇÃO DO SISTEMA]\n"
                f"{contexto}\n\n"
            )
        
        prompt_base += (
            f"Gere 3 cenários de teste no formato BDD (Dado, Quando, Então) em português.\n"
            f"Responda apenas com uma lista de strings, sem explicações."
        )
        
        return prompt_base


class OpenAIResponseProcessor:
    """Responsável por processar respostas da OpenAI"""
    
    @staticmethod
    def process_response(content: str) -> List[str]:
        if not content or not content.strip():
            raise GeradorTesteException("Resposta vazia recebida da OpenAI")
        
        linhas = [linha.strip() for linha in content.split("\n") if linha.strip()]
        
        if not linhas:
            raise GeradorTesteException("Nenhum cenário de teste foi gerado")
            
        return linhas


class ContextRetriever:
    """Responsável por recuperar contexto vetorizado"""
    
    def __init__(self, vector_service=None):
        self._vector_service = vector_service
    
    def retrieve_context(self, historia: HistoriaUsuario, max_docs: int = 3) -> str:
        """Recupera contexto relevante baseado na história de usuário"""
        if not self._vector_service:
            return ""
        
        try:
            contextos = self._vector_service.buscar_contexto(
                consulta=f"{historia.titulo} {historia.descricao}", 
                k=max_docs
            )
            return "\n\n".join(contextos) if contextos else ""
        except Exception:
            # Em caso de erro na busca, continua sem contexto
            return ""


class GeradorTesteOpenAI(GeradorTestePort):
    def __init__(self, modelo: str = None, vector_service=None):
        try:
            self._client = OpenAI(api_key=OpenAIConfig.get_api_key())
            self._modelo = modelo or OpenAIConfig.get_model()
            self._temperature = OpenAIConfig.get_temperature()
        except ValueError as e:
            raise ConfiguracaoInvalidaException(f"Erro na configuração da OpenAI: {e}")
        
        self._prompt_builder = PromptBuilder()
        self._response_processor = OpenAIResponseProcessor()
        self._context_retriever = ContextRetriever(vector_service)

    def gerar_teste(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        # Recuperar contexto vetorizado (RAG)
        contexto = self._context_retriever.retrieve_context(historia)
        
        # Construir prompt com contexto
        prompt = self._prompt_builder.build_teste_prompt(historia, contexto)
        
        try:
            resposta = self._client.chat.completions.create(
                model=self._modelo,
                messages=[
                    {"role": "system", "content": "Você é um especialista em QA que gera testes baseados em documentação existente."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self._temperature
            )
            
            conteudo = resposta.choices[0].message.content.strip()
            cenarios = self._response_processor.process_response(conteudo)
            
            return TesteGeradoOutput(
                resumo=historia.resumo(),
                cenarios_bdd=cenarios
            )
        except Exception as e:
            if isinstance(e, GeradorTesteException):
                raise
            raise GeradorTesteException(f"Erro ao gerar teste com OpenAI: {e}")
