import sqlite3

conn = sqlite3.connect('weather_history.db') # podkluchaemsya k nashemy db
cursor = conn.cursor()

cursor.execute("SELECT * FROM weather") #pishem zapros vybrat' vse iz tablicy weather

rows = cursor.fetchall() # dostaem vse stroki kotorie nashel sql

print("ID | Город | Температура | Дата и время")
print("-" * 50)
for row in rows:
    print(f"В городе {row[1]} сейчас {row[2]} градусов")

conn.close()

