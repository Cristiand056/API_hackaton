import shutil
from tempfile import NamedTemporaryFile
from typing import Annotated
from fastapi import APIRouter, Depends, File, HTTPException, Path, UploadFile
from config.db import SessionLocal, conn
from models.riesgos_gestion import riegosgestion, GestionRiesgos 
from schemas.gestion_riesgos import GestionRiesgosSchema
from schemas.gestion_riesgos_update import GestionRiesgosSchemaUpdate 
from convertidor.excel_to_sql import covertir
from sqlalchemy.orm import Session

import bcrypt
sal = bcrypt.gensalt()

gestion = APIRouter()

@gestion.get("/riesgosgestion-ver")
async def get_riesgos_gestion():
    db = SessionLocal()
    try:     
        lista = db.query(GestionRiesgos).all()
        return lista
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()
        
@gestion.get("/riesgosgestion-ver-con-referencia/{referencia_ingresada}")
async def get_riesgos_gestion_referencia(referencia_ingresada):
    db = SessionLocal()
    try:     
        consulta = db.query(GestionRiesgos).filter(GestionRiesgos.referencia==referencia_ingresada).first()
        if consulta is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            return consulta
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()

@gestion.post("/riesgosgestion-crear")
async def crear_riesgos_gestion(gestionries: GestionRiesgosSchema):
    db = SessionLocal()
    
    #"responable" :bcrypt.hashpw(gestionries.responsable.encode('utf-8'), sal),
    try:     
        """
        intento = dict(list(gestionries))
        result = conn.execute(riegosgestion.insert().values(intento)) 
        conn.commit()
        created_id = result.inserted_primary_key
        
        return {"message": "Registro creado exitosamente", "id": created_id}
        """    
        intento2 = GestionRiesgos(**gestionries.dict())
        db.add(intento2)
        db.commit()
        
        return "Registro creado"
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el registro: {str(e)}")
    finally:
        db.close()


@gestion.patch("/riesgosgestion-act/{referencia_ingresada}")
async def del_riesgos_gestion(referencia_ingresada, update_referencia:GestionRiesgosSchemaUpdate):
    db = SessionLocal()
    try:     
        act_referencia = db.query(GestionRiesgos).filter(GestionRiesgos.referencia==referencia_ingresada).first()
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

@gestion.delete("/riesgosgestion-borrado/{referencia_ingresada}")
async def del_riesgos_gestion(referencia_ingresada):
    db = SessionLocal()
    try:     
        borrado = db.query(GestionRiesgos).filter(GestionRiesgos.referencia==referencia_ingresada).first()
        if borrado is None:
            HTTPException(status_code=404, detail="Referencia no encontrada")
        else:
            db.delete(borrado)
            db.commit()
            return "Regisitro eliminado con exito"
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()

@gestion.post("/subir-excel-gestion-riesgos")
async def subir_excel(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix

    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = Path(tmp.name)
    covertir("riegos-gestion", "")
    return "archivo subido"