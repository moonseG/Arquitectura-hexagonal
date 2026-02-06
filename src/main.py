from fastapi import FastAPI
from infrastructure.api.receta_controller import router
from infrastructure.api.user_controller import router as router

app = FastAPI(titlle="Microservicio Usuarios")
app.include_router(router)

"""@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}"""
