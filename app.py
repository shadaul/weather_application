#from pogoda.py - key and city
from location import find_location
from pogoda import getpogoda
from dotenv import load_dotenv
import os

load_dotenv()
KEY_POGODA=os.getenv("apikey_pogoda")

my_city = find_location()
my_pogoda = getpogoda(city = my_city, key_pogoda = KEY_POGODA)

print(f'vash gorod {my_city}i poogoda {my_pogoda}')