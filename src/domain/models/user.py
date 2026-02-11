from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class PacienteStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Paciente(BaseModel):
    '''Entidad de dominio: Paciente'''
    idpaciente: str
    nombre: str
    email: str
    status: PacienteStatus = PacienteStatus.ACTIVE
    
    def active(self):
        '''Comportamiento de dominio'''
        self.status = PacienteStatus.ACTIVE
    
    def deactivate(self):
        self.status = PacienteStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == PacienteStatus.ACTIVE

class PacienteCreate(BaseModel):
    '''DTO para crear un usuario. Datos del usuario que se reciben desde el exterior'''
    nombre: str
    email: str

'''class UserUpdate(BaseModel):
    DTO para actualizar un usuario
    nombre: Optional[str] = None
    email: Optional[str] = None
    status: Optional[UserStatus] = None'''