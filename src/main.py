from fastapi import FastAPI
from infrastructure.adapters.input.rest.receta_controller import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}
