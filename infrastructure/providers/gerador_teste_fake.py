from core.usecases.ports.gerador_teste_port import GeradorTestePort
from core.entities.historia_usuario import HistoriaUsuario
from shared.models.teste_models import TesteGeradoOutput

class GeradorTesteFake(GeradorTestePort):
    def gerar_teste(self, historia: HistoriaUsuario) -> TesteGeradoOutput:
        return TesteGeradoOutput(
            resumo=historia.resumo(),
            cenarios_bdd=[
                f"Dado que {historia.descricao}",
                "Quando o usuário interage com a funcionalidade",
                "Então o sistema responde corretamente"]
        )