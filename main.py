from fastapi import FastAPI
from client import *  # Import the getLocNum function
from Backend import iachat
app = FastAPI()

@app.get("/getUbiByNum/{num}")
async def read_root(num: str):
    try:
        location = getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}


@app.get("/isThere/{num_telf}/{location}")
async def read_root(num_tlf: str,location):
    try:
        return is_there(num_tlf, location)
    except Exception as e:
        return {"error": str(e)}

@app.get("/questions/{data_animal}/{query}")
async def ia_reponse(data_animal,query):
    try:
        return iachat.ia_question(data_animal,query)
    except Exception as e:
        return {"error": str(e)}




