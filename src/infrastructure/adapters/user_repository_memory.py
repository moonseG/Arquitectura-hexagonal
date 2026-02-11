from typing import List, Optional
from uuid import uuid4
from domain.models.user import Paciente, PacienteCreate, PacienteStatus
from application.ports.output.Paciente_repository import Paciente_repository

class PacienteRepositoryMemory(Paciente_repository):
    '''Implementación en memoria del repositorio de usuarios'''

    def __init__(self):
        self.pacientes = {}

    def create(self, paciente: PacienteCreate) -> Paciente:
        paciente_id = str(uuid4())
        new_paciente = Paciente(
            idpaciente=paciente_id,
            nombre=paciente.nombre,
            email=paciente.email,
            status=PacienteStatus.ACTIVE,
        )
        self.pacientes[new_paciente.idpaciente] = new_paciente
        return new_paciente

    def find_by_id(self, paciente_id: str) -> Optional[Paciente]:
        return self.pacientes.get(paciente_id)

    def find_all(self) -> List[Paciente]:
        return list(self.pacientes.values())

    def find_by_email(self, email: str) -> Optional[Paciente]:
        for paciente in self.pacientes.values():
            if paciente.email == email:
                return paciente
        return None

    ''''def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        user = self.users.get(user_id)
        if not user:
            return None
        
        if user_data.nombre is not None:
            user.nombre = user_data.nombre
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.status is not None:
            user.status = user_data.status

        return user'''

    def delete(self, paciente_id: str) -> bool:
        return self.pacientes.pop(paciente_id, None) is not None