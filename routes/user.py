from fastapi import APIRouter
from models.users import users
from config.db import conn

user = APIRouter()

@user.get("/users-ver")
def helloworld():
    return conn.execute(users.select()).fetchall()

@user.post("/users-crear")
def helloworld():
    return "Hello world"

@user.get("/users")
def helloworld():
    return "Hello world"

@user.get("/users")
def helloworld():
    return "Hello world"