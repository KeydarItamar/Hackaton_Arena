import network_as_code as nac
from datetime import datetime, timedelta
LOCATION_HISTORY_FILE = "location_history.csv"  # Path to the CSV file
import csv
import time



NAC_TOKEN = "62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"

client = nac.NetworkAsCodeClient(token=NAC_TOKEN)

def getLocNum(numtelf: str) -> dict:
    """Retrieves the latitude and longitude of a device given its phone number."""
    try:
<<<<<<< HEAD
        device =  client.devices.get(phone_number=numtelf)
        location = device.location(max_age=60)
        return {"longitude": location.longitude, "latitude": location.latitude ,"radius":10_000}
    except Exception as e:
        raise ValueError(f"Error getting device location: {e}") from e

def is_there(device_num: str, location: dict):   
    device = client.devices.get(phone_number=device_num)
    long= location['longitude']
    lat= location['latitude']
    radius= location['radius']
    return device.verify_location(long,lat,radius)
    # longitude=19, latitude=47, radius=10_000, max_age=60
    
    
# print(getLocNum('2143100025'))
=======
        device = client.devices.get(phone_number=numtelf)
        location = device.location(max_age=60)
        return {"longitude": location.longitude, "latitude": location.latitude}
    except Exception as e:
        raise ValueError(f"Error getting device location: {e}") from e

def is_there(device_num: str, longitude: float, latitude: float, radius: int = 10_000, max_age: int = 60) -> bool:
    """Checks if the device is within a specified radius of a location."""
    try:
        device = client.devices.get(phone_number=device_num)
        return device.verify_location(
            longitude=longitude, latitude=latitude, radius=radius, max_age=max_age
        )
    except Exception as e:
        raise ValueError(f"Error verifying device location: {e}") from e
<<<<<<< HEAD
>>>>>>> 5c53260c909f2d5a322ab44574b9a44587420017
=======
    
def save_location_history(device_num: str):
    while True:
        # Get location data from the function
        location = getLocNum(device_num)
 
        # Ensure successful retrieval before proceeding
        if not location:
            print("Error: Unable to retrieve location for device " + device_num + ". Skipping this iteration.")
            time.sleep(3600)  # Wait even if location retrieval fails
            continue

        # Extract data from the retrieved location
        timestamp = datetime.now().isoformat()
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Save the location data in the CSV file
        with open(LOCATION_HISTORY_FILE, "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, latitude, longitude])

        # Wait for the specified interval before next iteration
        time.sleep(3600)  # Convert minutes to seconds
>>>>>>> machine_learning
