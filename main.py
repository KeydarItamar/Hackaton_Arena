from fastapi import FastAPI
from client import getLocNum  # Import the getLocNum function

app = FastAPI()

@app.get("/getUbiByNum/{num}")
async def read_root(num: str):
    try:
        location = await getLocNum(num)
        return location
    except Exception as e:
        return {"error": str(e)}

<<<<<<< HEAD
# Example usage
num_telf = "34612345678"
location = getLocNum(num_telf)

if location is not None:
    print(f"Latitude: {location['latitude']}")
    print(f"Longitude: {location['longitude']}")
else:
    print("Unable to get device location.")
 
def is_there(device_num, data):   
    device = client.devices.get(phone_number=device_num)
    return device.verify_location(data)
    # longitude=19, latitude=47, radius=10_000, max_age=60

=======
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> marta
