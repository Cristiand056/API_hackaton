from fastapi import FastAPI
from routes.riesgos_gestion import gestion
from routes.user import user

app = FastAPI()

app.include_router(user)
app.include_router(gestion)



