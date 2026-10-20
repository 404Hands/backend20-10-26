from fastapi import FastAPI
from .apis.estudiante_rutas import router
app = FastAPI()

app.include_router(router =router, prefix='/api' \
'' )
