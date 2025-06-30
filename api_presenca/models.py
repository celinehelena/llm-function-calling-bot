from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Presenca(Base):
    __tablename__ = "presencas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_hours = Column(DateTime, default=datetime.now)
