import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
KEY_POGODA=os.getenv("apikey_pogoda")



def getpogoda(city, key_pogoda):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key_pogoda}&units=metric"
    
    response = requests.get(url)
    
    print(f"DEBUG: Status Code = {response.status_code}") 
    
    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        print(f"DEBUG: Server Response = {response.text}") 
        return "error"



# def getpogoda(city: str, key_pogoda: str):
    
#     url = f"http://api.weatherapi.com/v1/forecast.json"
#     params = {
#         "key": f"{key_pogoda}",
#         "q": city,
#         "days":3,
#         "aqi": "no",
#         "alerts": "no"
#     }

#     response = requests.get(url, params=params)
#     print("status code: ", response.status.code)
#     data = response.json()

#     if "error" in data:
#         return "error"
#     else:
#         return data["current"]["temp_c"]



# city = "Astana"
# city_temp = getpogoda(
#     city=city,
#     key_pogoda=KEY_POGODA
# )

# print(city)
# print(city_temp)