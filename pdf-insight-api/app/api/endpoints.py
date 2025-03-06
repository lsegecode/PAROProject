from fastapi import APIRouter, UploadFile, File
from app.services.pdf_processing import extract_text_from_pdf
from app.services.gemini_api import analyze_text_with_gemini

router = APIRouter()

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)

    # Si el PDF no tiene texto, devolvemos un error
    if not text.strip():
        return {"error": "No se pudo extraer texto del PDF. Asegúrate de que no sea un archivo escaneado."}

    # ✅ Pasamos el nombre del archivo correctamente
    analysis = analyze_text_with_gemini(file.filename, text)  

    return {"extracted_text": text, "analysis": analysis}
