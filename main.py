from fastapi import FastAPI
from client import getLocNum, is_there, save_location_history
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
