from typing import List, Optional
from domain.models.user import (Doctor, DoctorCreate, DoctorStatus)
from application.ports.output.Doctor_repository import Doctor_repository


class DoctorService:
    '''Servicio de aplicacion - casos de uso relacionados con User'''
    def __init__(self, repository: DoctorCreate):
        self.repository = repository

    def register_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        '''Caso de uso: Registrar un nuevo usuario'''
        #Validaciones de negocio
        if not doctor_data.nombre or not doctor_data.especialidad:
            raise ValueError("Username and especialidad are required")

        existing_doctores = self.repository.find_by_especialidad(doctor_data.especialidad)
        if existing_doctores:
            raise ValueError(f"Especialidad {doctor_data.especialidad} is already registered")

        #Crear user
        return self.repository.create(doctor_data)

    def get_doctor(self, idDoctor: str)-> Optional[Doctor]:
        return self.repository.find_by_id(doctor_id)

    def get_all_doctores(self) -> List[Doctor]:
        '''Caso de uso: Obtener todos los usuarios'''
        return self.repository.find_all()



    def delete_doctor(self, doctor_id: str) -> bool:
        '''Caso de uso: Eliminar un usuario'''
        return self.repository.delete(doctor_id)

    def desactive_doctor(self, doctor_id: str) -> Optional[Doctor]:
        '''Caso de uso: Desactivar un usuario'''
        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None

        doctor.deactivate()
        return self.repository.update(doctor_id, DoctorStatus(status=doctorStatus.INACTIVE))


    def get_doctor_status(self) -> dict:
        '''Caso de uso: Obtener estadisticas de usuarios'''
        Doctores = self.repository.find_all()
        Doctores = len(Doctores)
        active = len([u for u in Doctores if u.is_active()])

        return {
            "total_doctores": total,
            "active_doctores": active,
            "inactive_doctoress": total - active
        }