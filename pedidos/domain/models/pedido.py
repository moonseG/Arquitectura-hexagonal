from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class PedidoStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Pedido(BaseModel):
    idpedido: str
    nombrepedido: str
    status: PedidoStatus = PedidoStatus.ACTIVE
    
    def active(self):
        '''Comportamiento de dominio'''
        self.status = PedidoStatus.ACTIVE
    
    def deactivate(self):
        self.status = PedidoStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == PedidoStatus.ACTIVE

class PedidoCreate(BaseModel):
    nombrepedido: str

class PedidoUpdate(BaseModel):
    nombrepedido: Optional[str] = None
    status: Optional[PedidoStatus] = None