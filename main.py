from fastapi import FastAPI
<<<<<<< HEAD
from client import *  # Import the getLocNum function
from Backend import iachat
=======
from client import getLocNum, is_there

>>>>>>> 5c53260c909f2d5a322ab44574b9a44587420017
app = FastAPI()

@app.get("/getUbiByNum/{num}")
def read_root(num: str):
    try:
        location = getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}

<<<<<<< HEAD

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




=======
@app.get("/is_there/{device_num}/{longitude}/{latitude}")
def verify_location(device_num: str, longitude: float, latitude: float):
    radius=300
    try:
        is_within = is_there(device_num, longitude, latitude,radius)
        return {"device_present": is_within}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> 5c53260c909f2d5a322ab44574b9a44587420017
