from typing import Optional
from pydantic import BaseModel

def User(BaseModel):
    id: int
    name: str 
    password: str
    email: str
    role: str