from uuid import uuid4
from domain.models.pedido import Orden, OrdenStatus

class OrdenRepositoryMemory:

    def __init__(self):
        self.orders = {}

    def create(self, order_data):
        order = Order(
            idpedido=str(uuid4()),
            idusuario = order_data.idusuario,
            productos = order_data.productos,
            tltal +order_data.total,
            status = OrderStatus.CREADO
        )
        self.orders[order.idpedido] = order
        return order

    def find_all(self):
        return list(self.orders.values())

    def find_by_user(self, idusuario):
        return[o for o in self.orders.values() if o.idusuario == idusuario]

    def update_status(self, idpedido, status):
        order = self.orders.get(idpedido)
        if not order:
            return None
        order.status = status
        return order