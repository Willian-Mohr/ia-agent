from core.entities.historia_usuario import HistoriaUsuario
from shared.models.teste_models import TesteGeradoOutput

class GerarCenarioTesteUseCase:
    def execute(self, historia_usuario: HistoriaUsuario) -> TesteGeradoOutput:
        cenarios = [
            f"Dado que {historia_usuario.descricao}",
            "Quando o usuáro interage com a funcionalidade",
            "Então o sistema responde corretamente"
        ]
        return TesteGeradoOutput(
            resumo=historia_usuario.resumo(),
            cenarios_bdd=cenarios
        )