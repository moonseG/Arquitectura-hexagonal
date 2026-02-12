from fastapi import FastAPI
from infrastructure.controllers.pedido_controller import router as pedido_router

app = FastAPI(title="Microservicio Usuarios")

app.include_router(pedido_router)



"""@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}"""

