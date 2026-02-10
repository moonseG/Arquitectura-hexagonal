from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class User(BaseModel):
    '''Entidad de dominio: User'''
    idusuario: str
    nombre: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    
    def active(self):
        '''Comportamiento de dominio'''
        self.status = UserStatus.ACTIVE
    
    def deactivate(self):
        self.status = UserStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == UserStatus.ACTIVE

class UserCreate(BaseModel):
    '''DTO para crear un usuario. Datos del usuario que se reciben desde el exterior'''
    nombre: str
    email: str

class UserUpdate(BaseModel):
    '''DTO para actualizar un usuario'''
    nombre: Optional[str] = None
    email: Optional[str] = None
    status: Optional[UserStatus] = None