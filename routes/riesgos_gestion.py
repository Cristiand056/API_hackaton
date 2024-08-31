from typing import Annotated
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
import pandas as pd
from config.db import SessionLocal, get_db, engine
from models.riesgos_gestion import GestionRiesgos 
from schemas.gestion_riesgos import GestionRiesgosSchema
from schemas.gestion_riesgos_update import GestionRiesgosSchemaUpdate 
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
            return "Registro eliminado con exito"
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al ver el registro: {str(e)}")
    finally:
        db.close()

@gestion.post("/subir-excel-gestion-riesgos")
async def subir_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        
        df = pd.read_excel(file.file)
        
        """
        # Normalizar los nombres de las columnas
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('ó', 'o').str.replace('á', 'a')
        
        df = df.dropna(subset=[
            "proceso",
            "objetivo",
            "alcance",
            "impacto",
            "causa",
            "descripcion_oportunidad",
            "accion",
            "responsable",
            "fecha_seguimiento_primert",
            "seguimiento_primer_trimestre",
            "fecha_seguimiento_segundot",
            "seguimiento_segundo_trimestre",
            "fecha_seguimiento_tecerc",
            "seguimiento_tercer_trimestre",
            "fecha_seguimiento_cuartot",
            "seguimiento_cuarto_trimestre",
            "estado",
            "fecha_seguimiento_cys",
            "seguimiento_controly_sportes",
            "seguimiento_plan_manejo_oportunidades_y_soportes",
            "fecha_seguimiento_plan_manejo",
            "seguimento_plan_manejo_oportunidades",
            "estado_final"
        ], how='all')

        # Ahora los nombres de las columnas serán más fáciles de mapear
        column_mapping ={
             'proceso':'proceso', 
             'objetivo':'objetivo', 
             'alcance':'alcance', 
             'impacto':'impacto', 
             'causa':'causa',
             'descripcion_de_la_oportunidad':'descripcion_oportunidad',
             'accion':'accion', 
             'responsable':'responsable',
             'fecha_programada':'fecha_programada', 
             'fecha_seguimiento1':'fecha_seguimiento_primert',
             'seguimiento_primer_trimestre':'seguimiento_primer_trimestre', 
             'fecha_seguimiento2':'fecha_seguimiento_segundot',
             'seguimiento_segundo_trimestre':'seguimiento_segundo_trimestre', 
             'fecha_seguimiento3':'fecha_seguimiento_tecerc',
             'seguimiento_tercer_trimestre':'seguimiento_tercer_trimestre', 
             'fecha_seguimiento4':'fecha_seguimiento_cuartot',
             'seguimiento_cuarto_trimestre':'seguimiento_cuarto_trimestre', 
             'estado':'estado', 
             'fecha_seguimientose':'fecha_seguimiento_cys',
             'seguimiento_al_control_y_soportes':'seguimiento_controly_sportes',
             'seguimiento_al_plan_de_manejo_de_oportunidades_y_soportes':'seguimiento_plan_manejo_oportunidades_y_soportes',
             'fecha_seguimientoter':'fecha_seguimiento_plan_manejo',
             'seguimiento_al_plan_de_manejo_de_oportunidades':'seguimento_plan_manejo_oportunidades', 
             'estadoter':'estado_final'
        }
        
        
        
        for index, row in df.iterrows():
            # Crear una instancia del modelo
            gestion_riesgo = GestionRiesgos()

            # Asignar valores del DataFrame al modelo usando el mapeo
            for excel_column, model_field in column_mapping.items():
                setattr(gestion_riesgo, model_field, row[excel_column])

            # Agregar la instancia a la sesión
            db.add(gestion_riesgo)
        """
        df.to_sql(name="riesgos_gestion_data_vieja",con=engine, if_exists='append', index=False)
        
        db.commit()
        return f"message Archivo Excel subido y datos insertados correctamente"

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al procesar el archivo Excel: {str(e)}")
    finally:
        db.close()


