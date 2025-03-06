# 📄 PDF Insight API

API basada en **FastAPI** para analizar informes de partidos en formato **PDF**, extraer texto y generar insights mediante **Google Gemini AI**.

## 📌 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.9 o superior** 👉 [Descargar aquí](https://www.python.org/downloads/)
- **pip** (gestor de paquetes de Python)  
- **Virtualenv** para entornos virtuales  

---

## 🚀 **1️⃣ Crear y activar entorno virtual**
Para evitar conflictos entre paquetes, se recomienda usar un entorno virtual.

### 📌 **En Windows (CMD o PowerShell)**
python -m venv venv
venv\Scripts\activate

📌 En macOS / Linux
python3 -m venv venv
source venv/bin/activate

📦 2️⃣ Instalar dependencias
Ejecuta el siguiente comando en la terminal para instalar los paquetes requeridos:
pip install -r requirements.txt

⚙️ 3️⃣ Configurar las variables de entorno
El proyecto usa un archivo .env para almacenar claves API y configuraciones sensibles.

📌 Crear el archivo .env en la raíz del proyecto:
touch .env

📌 Contenido del archivo .env:
GEMINI_API_KEY=tu_clave_de_google_gemini
🔹 Reemplaza tu_clave_de_google_gemini con tu clave API de Google Gemini.

Si no tienes una clave API, puedes obtenerla en:
👉 Google AI Studio

▶️ 4️⃣ Ejecutar el servidor FastAPI
Después de instalar las dependencias y configurar el .env, ejecuta:
uvicorn app.main:app --reload
Esto iniciará el servidor en http://127.0.0.1:8000/.

📡 5️⃣ Probar la API en Postman o Swagger UI
FastAPI genera automáticamente documentación interactiva:

📌 Abrir en el navegador:
Swagger UI: 👉 http://127.0.0.1:8000/docs
Redoc: 👉 http://127.0.0.1:8000/redoc


🛠 Comandos Útiles

📌 Desactivar el entorno virtual:
deactivate

📌 Actualizar dependencias:
pip freeze > requirements.txt

🤝 Contribución
Si quieres mejorar el proyecto, puedes hacer un fork, trabajar en una rama y enviar un pull request.

🚀 ¡Gracias por usar PDF Insight API! 🎯



