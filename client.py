from fastapi import FastAPI
from client import getLocNum, is_there

app = FastAPI()

@app.get("/getUbiByNum/{num}")
def read_root(num: str):
    try:
        location = getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}

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
