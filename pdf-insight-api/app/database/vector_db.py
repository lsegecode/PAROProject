from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import create_engine
import threading

class DatabaseSingleton:
    """Clase Singleton para la gestión de la base de datos."""
    _instance = None
    _lock = threading.Lock()  

    def __new__(cls):
        """Evita que múltiples hilos creen más de una instancia"""
        with cls._lock:  
            if cls._instance is None:
                cls._instance = super(DatabaseSingleton, cls).__new__(cls)
                cls._instance.init_db()
        return cls._instance

    def init_db(self):
        """Inicializa la base de datos y la sesión."""
        DATABASE_URL = "sqlite:///./analisis.db"

        self.engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

        self.SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

        self.Base = declarative_base()

        # No llamamos create_tables() aquí para evitar import circular
        # Se ejecutará manualmente después

    def create_tables(self):
        """Crea las tablas en la base de datos si no existen."""
        from app.models.analysis import Analysis  # ⬅️ Importación dentro de la función
        self.Base.metadata.create_all(bind=self.engine)

    def get_db_session(self):
        """Devuelve una sesión de base de datos."""
        return self.SessionLocal()

# Crear una única instancia de la base de datos
db_instance = DatabaseSingleton()
Base = db_instance.Base
get_db_session = db_instance.get_db_session

# Llamamos a create_tables después de que todo esté inicializado
db_instance.create_tables()
