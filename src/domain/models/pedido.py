from pydantic import BaseModel
from enum import Enum
from typing import List
from uuid import uuid4 # Para generar IDs únicos de pedidos

class OrderStatus(str, Enum):
    CREADO = ""creado"
    PAGADO = "pagado"
    CANCELADO = "cancelado"

class Order(BaseModel): 
    idpedido: str
    idusuario: str
    productos: List[str]
    total: float
    status: OrdenStatus

class OrderCreate(BaseModel): # datos que manda Postman
    idusuario: str
    productos: List[str]
    total: float

class OrderUpdate(BaseModel):
    status: OrdenStatus