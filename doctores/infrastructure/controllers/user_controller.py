from fastapi import APIRouter, HTTPException
from domain.models.user import DoctorCreate
from application.services.user_services import DoctorService
from infrastructure.adapters.user_repository_memory import DoctorRepositoryMemory

router = APIRouter(prefix="/doctores", tags=["doctores"])

repository = DoctorRepositoryMemory()
service = DoctorService(repository)


@router.post("/")
def crear_doctor(doctor: DoctorCreate):
    try:
        return service.register_pacie(doctor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_doctores():
    return service.get_all_doctores()


@router.get("/{doctor_id}")
def obtener_doctor(doctor_id: str):
    doctor = service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor no encontrado")
    return doctor


@router.delete("/{doctor_id}")
def eliminar_doctor(doctor_id: str):
    if not service.delete_doctor(doctor_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}
