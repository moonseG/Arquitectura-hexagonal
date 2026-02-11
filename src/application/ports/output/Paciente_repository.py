from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.user import Paciente, PacienteCreate

class Paciente_repository(ABC):
    '''Puerto de salida: Repositorio de pacientes'''

    @abstractmethod
    def create(self, user: PacienteCreate) -> Paciente:
        '''Crea un nuevo usuario'''
        pass

    @abstractmethod
    def find_by_id(self, idpaciente: str) -> Optional[Paciente]:
        '''Obtiene un usuario por su ID'''
        pass

    @abstractmethod
    def find_all(self) -> List[Paciente]:
        '''Obtiene todos los pacientes'''
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Paciente]:
        '''Obtiene un usuario por su email'''
        pass

    '''@abstractmethod
    def update(self, idpaciente: str, paciente: PacienteUpdate) -> Optional[Paciente]:
        Actualiza un paciente existente
        pass'''

    @abstractmethod
    def delete(self, idpaciente: str) -> bool:
        '''Elimina un paciente por su ID'''
        pass