from abc import ABC, abstractmethod
from typing import List

class OrderRepository(ABC):
    
    @abstactmethod
    def create(self, order):
        pass
    
    @abstractmethod
    def find_all(self):
        pass
    
    @abstractmethod
    def find_by_user(self, idusuario: str):
        pass

    @abstractmethod
    def update_status(self, idpedido: str, status):
        pass