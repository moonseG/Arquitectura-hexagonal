from domain.models.receta import Receta
from domain.ports.input.consultar_receta_port import ConsultarRecetaPort

class ConsultarRecetaUseCase(ConsultarRecetaPort):

    def consultar(self, receta_id: int):
        receta = Receta(
            id=receta_id,
            equipo_base=[
                "Sartén de teflón",
                "Cuchillo de chef",
                "Espátula"
            ]
        )

        return {
            "mensaje": f"Consultando la receta {receta.id}",
            "equipo_base": receta.equipo_base
        }
