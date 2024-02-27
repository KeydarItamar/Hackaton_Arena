from fastapi import FastAPI
from typing import Union
from client import *
from main import *

app = FastAPI()


# @app.get("/")º
#     return {"Hello": "World"}


# @app.get("/getAllUbi")
# def read_root():
#     # return getAllUbi()
    
# @app.get("/getUbiByid/{id}")
# def read_root(id: int):
#     #  return getUbiBiId(id)
    
@app.get("/getUbiByNum/{num}")
def read_root(num: int):
    return getLocNum(num)
    