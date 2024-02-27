import network_as_code as nac
from network_as_code.models.device import Device, DeviceIpv4Addr
 
 
client = nac.NetworkAsCodeClient(
    token="b99a473d7bmsh05f095ca813f8b9p117072jsn40822e14f7be",
)

device = client.devices.get(phone_number = "2143100025"
                            
)

# ...and create a QoD session for the device


# Let's confirm that the device has the newly created session

print('datos del device:') 
print(device)



location = device.location(max_age=60)
 
longitude = location.longitude
latitude = location.latitude
 
 
print(longitude)
print(latitude)
print(location.civic_address)