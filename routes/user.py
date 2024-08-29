from fastapi import APIRouter
from models import users

user = APIRouter()

@user.get("/users")
def helloworld():
    return "Hello world"

@user.get("/users")
def helloworld():
    return "Hello world"

@user.get("/users")
def helloworld():
    return "Hello world"

@user.get("/users")
def helloworld():
    return "Hello world"