from typing import List, Optional
from uuid import uuid4
from domain.models.user import Doctor, DoctorCreate, DoctorStatus
from application.ports.output.Doctor_repository import Doctor_repository

class DoctorRepositoryMemory(Doctor_repository):

    def __init__(self):
        self.doctores = {}

    def create(self, doctor: DoctorCreate) -> Doctor:
        doctor_id = str(uuid4())
        new_doctor = Doctor(
            idDoctor=doctor_id,
            nombre=doctor.nombre,
            especialidad=doctor.especialidad,
            status=DoctorStatus.ACTIVE,
        )
        self.doctores[new_doctor.idDoctor] = new_doctor
        return new_doctor

    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        return self.doctores.get(doctor_id)

    def find_all(self) -> List[Doctor]:
        return list(self.doctores.values())

    def find_by_especialidad(self, especialidad: str) -> Optional[Doctor]:
        for doctor in self.doctores.values():
            if doctor.especialidad == especialidad:
                return doctor
        return None


    def delete(self, doctor_id: str) -> bool:
        return self.doctores.pop(doctor_id, None) is not None