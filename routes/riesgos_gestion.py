import shutil
from tempfile import NamedTemporaryFile
from typing import Annotated
from fastapi import APIRouter, Depends, File, HTTPException, Path, UploadFile
import pandas as pd
from config.db import SessionLocal, conn, get_db
from models.riesgos_gestion import riegosgestion, GestionRiesgos 
from schemas.gestion_riesgos import GestionRiesgosSchema
from schemas.gestion_riesgos_update import GestionRiesgosSchemaUpdate 
from convertidor.excel_to_sql import covertir
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from routes.user import oauth2_scheme

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
async def crear_riesgos_gestion( gestionries: GestionRiesgosSchema, token:str = Depends(oauth2_scheme)):
    db = SessionLocal()
    print(token)
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
async def subir_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Leer el archivo Excel en un DataFrame de pandas
        df = pd.read_excel(file.file)

        # Iterar sobre las filas del DataFrame y agregar cada una a la base de datos
        for _, row in df.iterrows():
            gestion_riesgos = GestionRiesgos(
                proceso=row.get("proceso"),
                objetivo=row.get("objetivo"),
                alcance=row.get("alcance"),
                impacto=row.get("impacto"),
                causa=row.get("causa"),
                descripcion_oportunidad=row.get("descripcion_oportunidad"),
                accion=row.get("accion"),
                responsable=row.get("responsable"),
                fecha_seguimiento_primert=pd.to_datetime(row.get("fecha_seguimiento_primert"), errors='coerce').date(),
                seguimiento_primer_trimestre=row.get("seguimiento_primer_trimestre"),
                fecha_seguimiento_segundot=pd.to_datetime(row.get("fecha_seguimiento_segundot"), errors='coerce').date(),
                seguimiento_segundo_trimestre=row.get("seguimiento_segundo_trimestre"),
                fecha_seguimiento_tecerc=pd.to_datetime(row.get("fecha_seguimiento_tecerc"), errors='coerce').date(),
                seguimiento_tercer_trimestre=row.get("seguimiento_tercer_trimestre"),
                fecha_seguimiento_cuartot=pd.to_datetime(row.get("fecha_seguimiento_cuartot"), errors='coerce').date(),
                seguimiento_cuarto_trimestre=row.get("seguimiento_cuarto_trimestre"),
                estado=row.get("estado"),
                fecha_seguimiento_cys=pd.to_datetime(row.get("fecha_seguimiento_cys"), errors='coerce').date(),
                seguimiento_controly_sportes=row.get("seguimiento_controly_sportes"),
                seguimiento_plan_manejo_oportunidades_y_soportes=row.get("seguimiento_plan_manejo_oportunidades_y_soportes"),
                fecha_seguimiento_plan_manejo=pd.to_datetime(row.get("fecha_seguimiento_plan_manejo"), errors='coerce').date(),
                seguimento_plan_manejo_oportunidades=row.get("seguimento_plan_manejo_oportunidades"),
                estado_final=row.get("estado_final")
            )

        # Añadir el objeto a la sesión
        db.add(gestion_riesgos)
        
        # Confirmar todos los cambios
        db.commit()
        
        return {"message": "Archivo Excel subido y datos insertados correctamente"}
    except Exception as e:
        db.rollback()  # Revertir cualquier cambio en caso de error
        raise HTTPException(status_code=400, detail=f"Error al procesar el archivo Excel: {str(e)}")
    finally:
        db.close()


