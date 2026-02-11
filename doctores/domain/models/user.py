from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class DoctorStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Doctor(BaseModel):
    idDoctor: str
    nombre: str
    especialidad: str
    status: DoctorStatus = DoctorStatus.ACTIVE
    
    def active(self):
        '''Comportamiento de dominio'''
        self.status = DoctorStatus.ACTIVE
    
    def deactivate(self):
        self.status = DoctorStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == DoctorStatus.ACTIVE

class DoctorCreate(BaseModel):
    '''DTO para crear un usuario. Datos del usuario que se reciben desde el exterior'''
    nombre: str
    especialidad: str
