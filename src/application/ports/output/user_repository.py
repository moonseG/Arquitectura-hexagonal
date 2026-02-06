from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.user import User, UserCreate, UserUpdate

class UserRepository(ABC):
    '''Puerto de salida: Repositorio de usuarios'''

    @abstractmethod
    def create(self, user: UserCreate) -> User:
        '''Crea un nuevo usuario'''
        pass

    @abstractmethod
    def find_by_id(self, idusuario: str) -> Optional[User]:
        '''Obtiene un usuario por su ID'''
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        '''Obtiene todos los usuarios'''
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        '''Obtiene un usuario por su email'''
        pass

    @abstractmethod
    def update(self, idusuario: str, user: UserUpdate) -> Optional[User]:
        '''Actualiza un usuario existente'''
        pass

    @abstractmethod
    def delete(self, idusuario: str) -> bool:
        '''Elimina un usuario por su ID'''
        pass