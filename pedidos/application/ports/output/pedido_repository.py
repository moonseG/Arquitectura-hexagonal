from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.pedido import Pedido, PedidoCreate, PedidoUpdate, PedidoStatus

class PedidoRepository(ABC):
    '''Puerto de salida: Repositorio de usuarios'''

    @abstractmethod
    def create(self, pedido: PedidoCreate) -> Pedido:
        pass

    @abstractmethod
    def find_by_id(self, idpedido: str) -> Optional[Pedido]:
        pass

    @abstractmethod
    def find_all(self) -> List[Pedido]:
        pass

    @abstractmethod
    def update(self, idpedido: str, pedido: PedidoUpdate) -> Optional[Pedido]:
        pass

    @abstractmethod
    def delete(self, idpedido: str) -> bool:
        pass