from fastapi import APIRouter
from config.db import conn
from models.riesgos_gestion import riegosgestion 
from schemas.gestion_riesgos import GestionRiegos

import bcrypt
sal = bcrypt.gensalt()

gestion = APIRouter()

@gestion.get("/riesgosgestion-ver")
def get_riesgos_gestion():
    return conn.execute(riegosgestion.select()).fetchall()

@gestion.post("/riesgosgestion-crear")
def crear_riesgos_gestion(gestionries: GestionRiegos):
    new_formato = {"referencia": gestionries.referencia, "estado final":gestionries.EstadoFinal}
    new_formato["responable"] = bcrypt.hashpw(gestionries.responsable.encode('utf-8'), sal)
    print(new_formato)
    return "creado no implementado aún"

@gestion.delete("/riesgosgestion-borrado")
def del_riesgos_gestion():
    return "borrado no implementado aún"

@gestion.delete("/riesgosgestion-borrado")
def del_riesgos_gestion():
    return "borrado no implementado aún"