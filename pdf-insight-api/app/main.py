from fastapi import FastAPI
from app.services.gemini_api import analyze_text_with_gemini, get_all_analyses
from app.api.endpoints import router

app = FastAPI()

app.include_router(router)


@app.post("/analyze/")
def analyze_pdf(nombre_pdf: str, texto: str):
    """Recibe un PDF y devuelve el análisis."""
    resultado = analyze_text_with_gemini(nombre_pdf, texto)
    return {"archivo": nombre_pdf, "analisis": resultado}

@app.get("/analyses/")
def get_analyses():
    """Devuelve todos los análisis guardados."""
    return get_all_analyses()
