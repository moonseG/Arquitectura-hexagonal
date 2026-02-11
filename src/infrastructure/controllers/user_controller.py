from fastapi import APIRouter, HTTPException
from domain.models.user import PacienteCreate
from application.services.user_services import PacienteService
from infrastructure.adapters.user_repository_memory import PacienteRepositoryMemory

router = APIRouter(prefix="/pacientes", tags=["pacientes"])

repository = PacienteRepositoryMemory()
service = PacienteService(repository)


@router.post("/")
def crear_paciente(paciente: PacienteCreate):
    try:
        return service.register_paciente(paciente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_pacientes():
    return service.get_all_pacientes()


@router.get("/{paciente_id}")
def obtener_paciente(paciente_id: str):
    paciente = service.get_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return paciente


@router.delete("/{paciente_id}")
def eliminar_paciente(paciente_id: str):
    if not service.delete_paciente(paciente_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
