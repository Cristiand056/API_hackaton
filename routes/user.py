from fastapi import APIRouter, Depends
from models.users import users
from config.db import conn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

user = APIRouter()

oauth2_scheme = OAuth2PasswordBearer("/token")

@user.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username, form_data.password)
    return {
        "access_token": "Toamtito",
        "token_type":"bearer"
    }

