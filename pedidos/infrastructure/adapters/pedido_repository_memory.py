from typing import List, Optional
from uuid import uuid4
from domain.models.pedido import Pedido, PedidoCreate, PedidoUpdate, PedidoStatus
from application.ports.output.pedido_repository import PedidoRepository

class PedidoRepositoryMemory(PedidoRepository):

    def __init__(self):
        self.pedidos = {}

    def create(self, pedido: PedidoCreate) -> Pedido:
        pedido_id = str(uuid4())
        new_pedido = Pedido(
            idpedido=pedido_id,
            nombrepedido=pedido.nombrepedido,
            status=PedidoStatus.ACTIVE,
        )
        self.pedidos[new_pedido.idpedido] = new_pedido
        return new_pedido

    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        return self.pedidos.get(pedido_id)

    def find_all(self) -> List[Pedido]:
        return list(self.pedidos.values())

    def update(self, pedido_id: str, pedido_data: PedidoUpdate) -> Optional[Pedido]:
        pedido = self.pedidos.get(pedido_id)
        if not pedido:
            return None
        
        if pedido_data.nombrepedido is not None:
            pedido.nombrepedido = pedido_data.nombrepedido
        if pedido_data.status is not None:
            pedido.status = pedido_data.status

        return pedido

    def delete(self, pedido_id: str) -> bool:
        return self.pedidos.pop(pedido_id, None) is not None