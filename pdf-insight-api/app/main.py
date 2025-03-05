from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="PDF Insight API", version="1.0")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "¡Bienvenido a PDF Insight API!"}
