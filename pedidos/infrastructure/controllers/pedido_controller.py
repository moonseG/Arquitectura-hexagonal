from fastapi import APIRouter, HTTPException
from domain.models.pedido import PedidoCreate, PedidoUpdate
from application.services.pedido_services import PedidoService
from infrastructure.adapters.pedido_repository_memory import PedidoRepositoryMemory

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

repository = PedidoRepositoryMemory()
service = PedidoService(repository)


@router.post("/")
def crear_pedido(pedido: PedidoCreate):
    try:
        return service.register_pedido(pedido)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_pedidos():
    return service.get_all_pedidos()


@router.get("/{pedido_id}")
def obtener_pedido(pedido_id: str):
    pedido = service.get_pedido(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido


@router.put("/{pedido_id}")
def actualizar_pedido(pedido_id: str, pedido: PedidoUpdate):
    updated = service.update_pedido(pedido_id, pedido)
    if not updated:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return updated


@router.delete("/{pedido_id}")
def eliminar_pedido(pedido_id: str):
    if not service.delete_pedido(pedido_id):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"mensaje": "Pedido eliminado"}
