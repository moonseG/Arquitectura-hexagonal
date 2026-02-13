from typing import List, Optional
from domain.models.pedido import (Pedido, PedidoCreate, PedidoUpdate, PedidoStatus)
from application.ports.output.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repository: PedidoCreate):
        self.repository = repository

    def register_pedido(self, pedido_data: PedidoCreate) -> Pedido:
        #Validaciones de negocio
        if not pedido_data.nombrepedido:
            raise ValueError("Username are required")

        #Crear user
        return self.repository.create(pedido_data)

    def get_pedido(self, pedido_id: str)-> Optional[Pedido]:
        '''Caso de uso: Obtener un usuario por su ID'''
        return self.repository.find_by_id(pedido_id)

    def get_all_pedidos(self) -> List[Pedido]:
        '''Caso de uso: Obtener todos los usuarios'''
        return self.repository.find_all()

    def update_pedido(self, pedido_id: str, pedido_data: PedidoUpdate) -> Optional[Pedido]:
        '''Caso de uso: Actualizar un usuario existente'''
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None

        return self.repository.update(pedido_id, pedido_data)

    def delete_pedido(self, pedido_id: str) -> bool:
        '''Caso de uso: Eliminar un usuario'''
        return self.repository.delete(pedido_id)

    def desactive_pedido(self, pedido_id: str) -> Optional[Pedido]:
        '''Caso de uso: Desactivar un usuario'''
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None

        pedido.deactivate()
        return self.repository.update(pedido_id, PedidoStatus(status=pedidoStatus.INACTIVE))

    def active_pedido(self, pedido_id: str) -> Optional[Pedido]:
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None

        pedido.active()
        return self.repository.update(pedido_id, PedidoUpdate(status=pedidoStatus.ACTIVE))

    def get_pedido_stats(self) -> dict:
        pedidos = self.repository.find_all()
        pedidos = len(pedidos)
        active = len([u for u in pedidos if u.is_active()])

        return {
            "total_pedidos": total,
            "active_pedidos": active,
            "inactive_pedidos": total - active
        }