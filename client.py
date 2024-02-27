import network_as_code as nac

NAC_TOKEN = "62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"

client = nac.NetworkAsCodeClient(token=NAC_TOKEN)

async def getLocNum(numtelf: str) -> dict:
    """Retrieves the latitude and longitude of a device given its phone number."""
    try:
        device = await client.devices.get(phone_number=numtelf)
        location = await device.location(max_age=60)
        return {"longitude": location.longitude, "latitude": location.latitude}
    except Exception as e:
        raise ValueError(f"Error getting device location: {e}") from e
