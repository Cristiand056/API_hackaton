from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
import pandas as pd
from config.db import SessionLocal, get_db, engine
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.oportunidades import Oportunidad
from schemas.oportunidades_schema import OportunidadSchema

opor = APIRouter()

@opor.get("oportunidades-ver")
async def get_oportunidades(db: Session = Depends(get_db)):
    try:     
        lista = db.query(Oportunidad).all()
        return lista
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()
        
opor.get("/oportunidades-ver-referencia/{referencia_ingresada}")
async def get_riesgos_gestion_referencia(referencia_ingresada, db: Session = Depends(get_db)):
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
        
@opor.post("/oportunidades-crear")
async def crear_riesgos_gestion( oport: OportunidadSchema, db: Session = Depends(get_db)):
    try:     
         
        intento2 = Oportunidad(**oport.dict())
        db.add(intento2)
        db.commit()
        
        return "Registro creado"
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el registro: {str(e)}")
    finally:
        db.close()
        
@opor.patch("/oportunidad-act/{referencia_ingresada}")
async def del_riesgos_gestion(referencia_ingresada, update_referencia:OportunidadSchema, db: Session = Depends(get_db)):
    try:     
        act_referencia = db.query(Oportunidad).filter(Oportunidad.referencia==referencia_ingresada).first()
        if act_referencia is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        
        for key,value in update_referencia.dict(exclude_unset = True).items():
            setattr(act_referencia, key, value)

        db.commit()
        return" Referencia actualizada"
            
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error no se encuentra el registro: {str(e)}")
    finally:
        db.close()
        
@opor.delete("/riesgosgestion-borrado/{referencia_ingresada}")
async def del_riesgos_gestion(referencia_ingresada, db: Session = Depends(get_db)):
    db = SessionLocal()
    try:     
        borrado = db.query(Oportunidad).filter(Oportunidad.referencia==referencia_ingresada).first()
        if borrado is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            db.delete(borrado)
            db.commit()
            return "Registro eliminado con exito"
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()