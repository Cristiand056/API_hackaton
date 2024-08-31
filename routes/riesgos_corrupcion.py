from fastapi import APIRouter
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
import pandas as pd
from config.db import SessionLocal, get_db, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.riesgo_corrupcion import GestionCorrupcion

corrupcion = APIRouter()

@corrupcion.get("/ver-riesgos-corrupcion")
async def get_riegos_corrupcion(db: Session = Depends(get_db)):
    try:     
        lista = db.query(GestionCorrupcion).all()
        return lista
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()
        
@corrupcion.get("/ver-riesgos-corrupcion-referencia/{referencia_ingresada}")
async def get_riesgos_gestion_referencia(referencia_ingresada, db: Session = Depends(get_db)):
    db = SessionLocal()
    try:     
        consulta = db.query(GestionCorrupcion).filter(GestionCorrupcion.referencia==referencia_ingresada).first()
        if consulta is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            return consulta
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()