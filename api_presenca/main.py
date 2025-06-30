from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

class PresencaCreate(BaseModel):
    nome: str

# Dependência para criar sessão
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/presenca")
def marcar_presenca(presenca: PresencaCreate, db: Session = Depends(get_db)):
    nova_presenca = models.Presenca(name=presenca.nome, date_hours=datetime.now())
    db.add(nova_presenca)
    db.commit()
    db.refresh(nova_presenca)
    return {"mensagem": f"Presença de {presenca.nome} registrada com sucesso."}

@app.get("/presenca")
def listar_presencas(db: Session = Depends(get_db)):
    presencas = db.query(models.Presenca).all()
    return [{"nome": p.name, "data_hora": p.date_hours.isoformat()} for p in presencas]
