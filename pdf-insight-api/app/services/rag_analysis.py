import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_with_chatgpt(text: str) -> str:
    """
    Envía el texto extraído a ChatGPT y devuelve un análisis del contenido.
    """
    prompt = f"Analiza el siguiente texto y dime de qué trata, menciona los puntos más importantes:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Cambiar a gpt-4-turbo
        messages=[
            {"role": "system", "content": "Eres un asistente experto en análisis de documentos."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content  # ✅ Cambiado a nueva sintaxis
