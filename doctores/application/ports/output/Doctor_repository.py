from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.user import Doctor, DoctorCreate

class Doctor_repository(ABC):

    @abstractmethod
    def create(self, user: DoctorCreate) -> Doctor:
        '''Crea un nuevo usuario'''
        pass

    @abstractmethod
    def find_by_id(self, idDoctor: str) -> Optional[Doctor]:
        '''Obtiene un usuario por su ID'''
        pass

    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def find_by_especialidad(self, especialidad: str) -> Optional[Doctor]:
        '''Obtiene un usuario por su email'''
        pass


    @abstractmethod
    def delete(self, idDoctor: str) -> bool:
        pass