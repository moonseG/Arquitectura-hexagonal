from fastapi import APIRouter, HTTPException
from domain.models.user import UserCreate, UserUpdate
from application.services.user_services import UserService
from infrastructure.adapters.user_repository_memory import UserRepositoryMemory

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

repository = UserRepositoryMemory()
service = UserService(repository)


@router.post("/")
def crear_usuario(user: UserCreate):
    try:
        return service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_usuarios():
    return service.get_all_users()


@router.get("/{user_id}")
def obtener_usuario(user_id: str):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.put("/{user_id}")
def actualizar_usuario(user_id: str, user: UserUpdate):
    updated = service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{user_id}")
def eliminar_usuario(user_id: str):
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
