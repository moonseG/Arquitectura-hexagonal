from fastapi import APIRouter
from application.use_cases.consultar_receta import ConsultarRecetaUseCase

router = APIRouter()
use_case = ConsultarRecetaUseCase()

@router.get("/receta/{receta_id}")
def get_receta(receta_id: int):
    return use_case.consultar(receta_id)
