
# Pet Pulls: Track and Understand Your Furry Friend 

A mobile app for enhanced pet safety, well-being, and understanding.


## Documentation

### Features:

### Real-time pet tracking:  
Locate your furry friend with confidence using our reliable location tracking powered by Nokia's Network as Code APIs.
### AI-powered insights: 
Gain personalized understanding of your pet's behavior and needs through the integration of LangChain library and Cohere model, fostering stronger bonds and better care.
### Comprehensive pet profile: 
Manage all your pet's vital information in one central location, including medical records, vaccination history, and photos, ensuring accessibility and preparedness.
### Community building: 
Connect with other pet owners in your area for pet-sitting, socialization, and emergency support, fostering a supportive and connected community.
## API Reference

#### Retrieves the current latitude and longitude of a device based on its phone number.

```http
GET /getUbiByNum/{num}
```


#### Checks whether a device is within a specified radius (in meters) of a given location.

```http
GET /is_there/{device_num}/{longitude}/{latitude}/{radius}
```


#### Retrieves the location of a device at a specified interval and saves it to a CSV file

```http
GET /save_location_history/{device_num}
```



#### Attempts to create a QoD (Quality of Service) session for a device based on its phone number, supposedly used for emergency situations.

```http
GET /open_qod_emergenc/{device_num}
```



#### Generate AI-powered responses to pre-defined pet-related questions based on provided animal data.

```http
GET /questions/{data_animal}/{num}
```



## 🛠 Tech Stack

**Client:** Swift

**Server:** Python, Fast API, LangChain library, Cohere API


![Escudo de Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Escudo de Swift](https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white)



## Authors

- [@KeydarItamar](https://github.com/KeydarItamar)
- [@Marta Mateu](https://github.com/martamateu)
- [@Jordi]()
- [@Reinier]()

## Acknowledgements

 - [Nokia's Network as Code](https://developer.networkascode.nokia.io/docs)






![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

