#from pogoda.py - key and city
from location import find_location
from pogoda import getpogoda
from dotenv import load_dotenv
import os
import sqlite3

db_connection = sqlite3.connect('weather_history.db')
cursor = db_connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS weather(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               city TEXT,
               temperature REAL,
               date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )
''')
db_connection.commit()

#INTEGER PRIMARY KEY AUTOINCREMENT уникальный номер создать
#text i real eto tipy dannyh, gorod eto text a temperatura eto drobnoe chislo
#DEFAULT CURRENT_TIMESTAMP baza sama postavit vremya i daty kogda dobavim zapis'
#db_connection.commit() chtoby sohranit' deistvya



load_dotenv()
KEY_POGODA=os.getenv("apikey_pogoda")

my_city = find_location()
my_pogoda = getpogoda(city = my_city, key_pogoda = KEY_POGODA)

print(f'vash gorod {my_city}i poogoda {my_pogoda}')

sql_query = "INSERT INTO weather (city, temperature) VALUES (?, ?)" #prosim vstavit' v tablicu v kolonki city i temperature znachenia ?
cursor.execute(sql_query, (my_city, my_pogoda)) # peredaem dannie vmesto ?
db_connection.commit()
print("Данные успешно сохранены в базу!")
db_connection.close() #zakrivaem v konce
