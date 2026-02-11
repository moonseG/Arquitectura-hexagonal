from fastapi import FastAPI
from infrastructure.controllers.user_controller import router as user_router
from infrastructure.controllers.user_controller import router as doctor_router

app = FastAPI(title="Microservicio Doctores")


app.include_router(doctor_router)



"""@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}"""

