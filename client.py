import network_as_code as nac

NAC_TOKEN = "62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"

client = nac.NetworkAsCodeClient(token=NAC_TOKEN)

def getLocNum(numtelf: str) -> dict:
    """Retrieves the latitude and longitude of a device given its phone number."""
    try:
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
