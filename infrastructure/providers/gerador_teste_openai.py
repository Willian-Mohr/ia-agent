import openai
from openai import OpenAI

from core.usecases.ports.gerador_teste_port import GeradorTestePort
from core.entities.historia_usuario import HistoriaUsuario
from shared.models.teste_models import TesteGeradoOutput
from shared.config.env import OPENAI_API_KEY

class GeradorTesteOpenAI(GeradorTestePort):
    def __init__(self, modelo: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.modelo = modelo
        
    def gerar_teste(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        prompt = (
            f"Com base na seguinte história de usuário:\n\n"
            f"Título: {historia.titulo}\n"
            f"Descrição: {historia.descricao}\n\n"
            f"Gere 3 cenários de teste no formato BDD (Dado, Quando, Então) em português.\n"
            f"Responda apenas com uma lista de strings, sem explicações."
        )
        
        try:
            resposta = self.client.chat.completions.create(
                model=self.modelo,
                messages=[
                    {"role": "system", "content": "Você é um especialista em QA."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            conteudo = resposta.choices[0].message.content.strip()
            linhas = [linha.strip() for linha in conteudo.split("\n") if linha.strip()]
            
            return TesteGeradoOutput(
                resumo=historia.resumo(),
                cenarios_bdd=linhas
            )
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar teste com OpenAI: {e}")