from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
import pandas as pd
from config.db import SessionLocal, get_db, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.oportunidades import Oportunidad

opor = APIRouter()

@opor.get("oportunidades-ver")
async def get_seguridad(db: Session = Depends(get_db)):
    try:     
        lista = db.query(Oportunidad).all()
        return lista
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()
        
opor.get("/oportunidades-ver-referencia/{referencia_ingresada}")
async def get_riesgos_gestion_referencia(referencia_ingresada):
    db = SessionLocal()
    try:     
        consulta = db.query(Oportunidad).filter(Oportunidad.referencia==referencia_ingresada).first()
        if consulta is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            return consulta
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()