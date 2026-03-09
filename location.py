import requests
from pprint import pprint
from findip import get_myip

def find_location():
    ip = get_myip()
    url = f"https://free.freeipapi.com/api/json/{ip}"



    response = requests.get(url)
    data = response.json()

    return data["capital"]

myloc = find_location()
print(myloc)