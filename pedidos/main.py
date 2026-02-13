from fastapi import FastAPI
from infrastructure.controllers.pedido_controller import router as pedido_router

app = FastAPI(title="Microservicio Pedidos")

app.include_router(pedido_router)


