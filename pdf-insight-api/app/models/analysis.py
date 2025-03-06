from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database.vector_db import Base

class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_pdf = Column(String(255), nullable=False)
    analisis = Column(Text, nullable=False)
    fecha = Column(DateTime, default=func.now())

