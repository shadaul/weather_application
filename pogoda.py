import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
KEY_POGODA=os.getenv("apikey_pogoda")



def getpogoda(city: str, key_pogoda: str):
    
    url = f"http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": f"{key_pogoda}",
        "q": city,
        "days":3,
        "aqi": "no",
        "alerts": "no"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "error" in data:
        return "error"
    else:
        return data["current"]["temp_c"]



# city = "Astana"
# city_temp = getpogoda(
#     city=city,
#     key_pogoda=KEY_POGODA
# )

# print(city)
# print(city_temp)