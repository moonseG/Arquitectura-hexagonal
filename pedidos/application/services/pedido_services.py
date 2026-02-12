from typing import List, Optional
from domain.models.user import (User, UserCreate, UserUpdate, UserStatus)
from application.ports.output.user_repository import UserRepository

class UserService:
    '''Servicio de aplicacion - casos de uso relacionados con User'''
    def __init__(self, repository: UserCreate):
        self.repository = repository

    def register_user(self, user_data: UserCreate) -> User:
        '''Caso de uso: Registrar un nuevo usuario'''
        #Validaciones de negocio
        if not user_data.nombre or not user_data.email:
            raise ValueError("Username and email are required")

        #Verificar unicidad del email
        existing_users = self.repository.find_by_email(user_data.email)
        if existing_users:
            raise ValueError(f"Email {user_data.email} is already registered")

        #Crear user
        return self.repository.create(user_data)

    def get_user(self, user_id: str)-> Optional[User]:
        '''Caso de uso: Obtener un usuario por su ID'''
        return self.repository.find_by_id(user_id)

    def get_all_users(self) -> List[User]:
        '''Caso de uso: Obtener todos los usuarios'''
        return self.repository.find_all()

    def update_user(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        '''Caso de uso: Actualizar un usuario existente'''
        user = self.repository.find_by_id(user_id)
        if not user:
            return None

        #AValidar que el nuevo email no este en uso por otro usuario
        if user_data.email and user_data.email != user.email:
            existing_users = self.repository.find_by_email(user_data.email)
            if existing_users:
                raise ValueError(f"Email {user_data.email} is already registered")

        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id: str) -> bool:
        '''Caso de uso: Eliminar un usuario'''
        return self.repository.delete(user_id)

    def desactive_user(self, user_id: str) -> Optional[User]:
        '''Caso de uso: Desactivar un usuario'''
        user = self.repository.find_by_id(user_id)
        if not user:
            return None

        user.deactivate()
        return self.repository.update(user_id, UserStatus(status=userStatus.INACTIVE))

    def active_user(self, user_id: str) -> Optional[User]:
        '''Caso de uso: Activar un usuario'''
        user = self.repository.find_by_id(user_id)
        if not user:
            return None

        user.active()
        return self.repository.update(user_id, UserUpdate(status=userStatus.ACTIVE))

    def get_user_stats(self) -> dict:
        '''Caso de uso: Obtener estadisticas de usuarios'''
        users = self.repository.find_all()
        users = len(users)
        active = len([u for u in users if u.is_active()])

        return {
            "total_users": total,
            "active_users": active,
            "inactive_users": total - active
        }