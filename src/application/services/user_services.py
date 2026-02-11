from typing import List, Optional
from domain.models.user import (Paciente, PacienteCreate, PacienteStatus)
from application.ports.output.Paciente_repository import Paciente_repository
#from application.ports.output.user_repository import UserRepository

class PacienteService:
    '''Servicio de aplicacion - casos de uso relacionados con User'''
    def __init__(self, repository: PacienteCreate):
        self.repository = repository

    def register_paciente(self, paciente_data: PacienteCreate) -> Paciente:
        '''Caso de uso: Registrar un nuevo usuario'''
        #Validaciones de negocio
        if not paciente_data.nombre or not paciente_data.email:
            raise ValueError("Username and email are required")

        #Verificar unicidad del email
        existing_users = self.repository.find_by_email(paciente_data.email)
        if existing_users:
            raise ValueError(f"Email {paciente_data.email} is already registered")

        #Crear user
        return self.repository.create(paciente_data)

    def get_paciente(self, idpaciente: str)-> Optional[Paciente]:
        '''Caso de uso: Obtener un usuario por su ID'''
        return self.repository.find_by_id(paciente_id)

    def get_all_pacientes(self) -> List[Paciente]:
        '''Caso de uso: Obtener todos los usuarios'''
        return self.repository.find_all()

    '''def update_user(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        Caso de uso: Actualizar un usuario existente
        user = self.repository.find_by_id(user_id)
        if not user:
            return None

        #AValidar que el nuevo email no este en uso por otro usuario
        if user_data.email and user_data.email != user.email:
            existing_users = self.repository.find_by_email(user_data.email)
            if existing_users:
                raise ValueError(f"Email {user_data.email} is already registered")

        return self.repository.update(user_id, user_data)'''

    def delete_paciente(self, paciente_id: str) -> bool:
        '''Caso de uso: Eliminar un usuario'''
        return self.repository.delete(paciente_id)

    def desactive_paciente(self, paciente_id: str) -> Optional[Paciente]:
        '''Caso de uso: Desactivar un usuario'''
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None

        paciente.deactivate()
        return self.repository.update(paciente_id, PacienteStatus(status=pacienteStatus.INACTIVE))

    ''''def active_paciente(self, paciente_id: str) -> Optional[Paciente]:
        Caso de uso: Activar un usuario
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None

        paciente.active()
        return self.repository.update(user_id, UserUpdate(status=userStatus.ACTIVE))'''

    def get_paciente_status(self) -> dict:
        '''Caso de uso: Obtener estadisticas de usuarios'''
        pacientes = self.repository.find_all()
        pacientes = len(pacientes)
        active = len([u for u in pacientes if u.is_active()])

        return {
            "total_pacientes": total,
            "active_pacientes": active,
            "inactive_pacientes": total - active
        }