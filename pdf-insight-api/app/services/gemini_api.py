import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar la API Key de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_text_with_gemini(text: str) -> str:
    """
    Envía el texto extraído a Google Gemini y devuelve un análisis del contenido.
    """
    model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Usa el modelo correcto
    response = model.generate_content(f"Analiza el siguiente texto y dime de qué trata:\n\n{text}")

    return response.text  # Devuelve el análisis generado
