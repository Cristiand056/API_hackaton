from fastapi import FastAPI
from config.db import SessionLocal
from routes.riesgos_gestion import gestion
from routes.user import user

app = FastAPI()


app.include_router(user)
app.include_router(gestion)



