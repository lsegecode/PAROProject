import google.generativeai as genai
import os
import logging
from dotenv import load_dotenv
from google.api_core.exceptions import GoogleAPIError
from sqlalchemy.orm import Session
from app.database.vector_db import get_db_session  # ⬅️ Usamos la sesión del Singleton
from app.models.analysis import Analysis

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logging.error("La clave de API de Gemini no está configurada. Verifica tu archivo .env.")
else:
    genai.configure(api_key=api_key)

def save_analysis(nombre_pdf: str, analisis: str):
    """Guarda el análisis en la base de datos SQLite usando la sesión del Singleton."""
    try:
        db: Session = get_db_session()  # ⬅️ Obtenemos la sesión del Singleton
        new_analysis = Analysis(nombre_pdf=nombre_pdf, analisis=analisis)
        db.add(new_analysis)
        db.commit()
        db.refresh(new_analysis)
        logging.info(f"Análisis guardado para el archivo: {nombre_pdf}")
    except Exception as e:
        logging.error(f"Error al guardar en la base de datos: {e}")
    finally:
        db.close()  # ⬅️ Aseguramos el cierre de la sesión para evitar bloqueos

def analyze_text_with_gemini(nombre_pdf: str, text: str) -> str:
    """
    Envía el texto extraído a Google Gemini y guarda el análisis en SQLite.
    """
    if not text or not isinstance(text, str):
        logging.error("El texto proporcionado no es válido.")
        return "Error: El texto de entrada no es válido."

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Analiza el siguiente texto y dime de qué trata:\n\n{text}")

        if not hasattr(response, "text") or not response.text:
            logging.warning("La respuesta de Gemini no contiene texto.")
            return "Error: No se obtuvo una respuesta válida del modelo."

        save_analysis(nombre_pdf, response.text)

        return response.text

    except GoogleAPIError as e:
        logging.error(f"Error en la API de Google Gemini: {e}")
        return "Error: No se pudo procesar la solicitud debido a un problema con la API de Google."

    except Exception as e:
        logging.exception(f"Ocurrió un error inesperado: {e}")
        return "Error: Se produjo un problema inesperado al analizar el texto."
    
def get_all_analyses():
    """Obtiene todos los análisis guardados en la base de datos."""
    try:
        from app.models.analysis import Analysis  # Importación diferida para evitar import circular
        db: Session = get_db_session()
        analyses = db.query(Analysis).all()
        db.close()
        return [{"id": a.id, "nombre_pdf": a.nombre_pdf, "analisis": a.analisis, "fecha": a.fecha} for a in analyses]
    except Exception as e:
        logging.error(f"Error al obtener los análisis: {e}")
        return []
