from fastapi import FastAPI
from infrastructure.controllers.receta_controller import router as receta_router
from infrastructure.controllers.user_controller import router as user_router

app = FastAPI(title="Microservicio Usuarios")

app.include_router(receta_router)
app.include_router(user_router)



"""@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}"""

