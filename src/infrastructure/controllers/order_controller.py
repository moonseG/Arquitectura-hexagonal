from fastapi import APIRouter, HTTPException

rouetr = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/")
def crear_pedido(order):
    try:
        return service.create_order(order)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
def listar_pedidos():
    return service.get_all()

@router.get("/usuario/{idusuario}"):
def pedidos_por_usuario(idusuario):
    return service.get_by_user(idusuario)

@router.put("/{idpedido"):
def actualizarr_estado(idpedido, status):
    pedido = service.update_status(idpedido, status)
    if nor pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido