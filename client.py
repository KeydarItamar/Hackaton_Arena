import network_as_code as nac

NAC_TOKEN = "62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"

client = nac.NetworkAsCodeClient(token=NAC_TOKEN)

def getLocNum(numtelf: str) -> dict:
    """Retrieves the latitude and longitude of a device given its phone number."""
    try:
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