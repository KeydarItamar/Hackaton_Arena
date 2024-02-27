
import network_as_code as nac 
client = nac.NetworkAsCodeClient(
    token="62ac7c527dmshe7f67ae0b9f3680p1bfae2jsnde0b639c225e"
)

def getLocNum(numtelf: str):
    device = client.devices.get(phone_number= numtelf)
    location = device.location(max_age=60)
    return location