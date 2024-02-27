
import network_as_code as nac 
from fastapi import FastAPI
from main import *

app = FastAPI()


    
@app.get("/getUbiByNum/{num}")
def read_root(num: int):
    return getLocNum(num)
    

client = nac.NetworkAsCodeClient(
    token="62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"
)

def getLocNum(numtelf: str):
    """
    Retrieves the latitude and longitude of a device given its phone number.

    Args:
        numtelf (str): Phone number of the device.

    Returns:
        dict: Dictionary with the keys "longitude" and "latitude".
    """
    try:
        device = client.devices.get(phone_number=numtelf)
        location = device.location(max_age=60)
        return {"longitude": location.longitude, "latitude": location.latitude}
    except Exception as e:
        print(f"Error getting device location: {e}")
        return None

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

