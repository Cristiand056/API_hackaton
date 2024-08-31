from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
import pandas as pd
from config.db import SessionLocal, get_db, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.riesgos_seguridad import RiesgosSeguridad

seguridad = APIRouter()

@seguridad.get("riesgos-seguridad-ver")
async def get_seguridad(db: Session = Depends(get_db)):
    try:     
        lista = db.query(RiesgosSeguridad).all()
        return lista
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()
        
seguridad.get("/riesgos-seguridad-ver-referencia/{referencia_ingresada}")
async def get_riesgos_gestion_referencia(referencia_ingresada):
    db = SessionLocal()
    try:     
        consulta = db.query(RiesgosSeguridad).filter(RiesgosSeguridad.referencia==referencia_ingresada).first()
        if consulta is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            return consulta
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()