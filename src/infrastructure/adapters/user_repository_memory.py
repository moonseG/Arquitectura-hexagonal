from typing import List, Optional
from uuid import uuid4
from domain.models.user import User, UserCreate, UserUpdate, UserStatus
from application.ports.output.user_repository import UserRepository

class UserRepositoryMemory(UserRepository):
    '''Implementación en memoria del repositorio de usuarios'''

    def __init__(self):
        self.users = {}

    def create(self, user: UserCreate) -> User:
        user_id = str(uuid4())
        new_user = User(
            idusuario=user_id,
            nombre=user.nombre,
            email=user.email,
            status=UserStatus.ACTIVE,
        )
        self.users[new_user.idusuario] = new_user
        return new_user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def find_all(self) -> List[User]:
        return list(self.users.values())

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        user = self.users.get(user_id)
        if not user:
            return None
        
        if user_data.nombre is not None:
            user.nombre = user_data.nombre
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.status is not None:
            user.status = user_data.status

        return user

    def delete(self, user_id: str) -> bool:
        return self.users.pop(user_id, None) is not None