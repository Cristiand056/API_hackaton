from fastapi import FastAPI
from config.db import SessionLocal
from routes.riesgos_gestion import gestion
from routes.user import user
from routes.riesgos_corrupcion import corrupcion
from routes.riesgos_seguridad import seguridad

app = FastAPI()


app.include_router(user)
app.include_router(gestion)
app.include_router(corrupcion)
app.include_router(seguridad)


