from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from client import *  # Import the getLocNum function
from Backend import iachat
from client import getLocNum, is_there, save_location_history
import json
LOCATION_HISTORY_FILE = "location_history.csv" 
import csv

app = FastAPI()

@app.get("/getUbiByNum/{num}")
def read_root(num: str):
    try:
        location = getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}


class AnimalData(BaseModel):
    data_animal: dict

@app.post("/questions")
async def ia_response(animal_data: AnimalData):
    try:
        return iachat.ia_question(animal_data.data_animal)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# @app.get("/questions/{data_animal}/{num}")
# async def ia_reponse(data_animal,num: int):
#     try:
#         return iachat.ia_question(data_animal,num)
#     except Exception as e:
#         return {"error": str(e)}


@app.get("/is_there/{device_num}/{longitude}/{latitude}/{radius}")
def verify_location(device_num: str, longitude: float, latitude: float, radius: int): 
    try:
        is_within = is_there(device_num, longitude, latitude, radius)
        return {"device_present": is_within}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/save_location_history/{device_num}")
def initiate_history(device_num: str):
    save_location_history(device_num)  # Call the imported function
    return {"message": "Location history saving started for device " + device_num}

        
        


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
