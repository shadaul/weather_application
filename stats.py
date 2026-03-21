import sqlite3

conn = sqlite3.connect('weather_history.db')
cursor = conn.cursor()


cursor.execute("SELECT AVG(temperature), MIN(temperature), MAX(temperature), count(*) FROM weather")
result = cursor.fetchone()

avg_t, min_t, max_t, count = result

print("----отчет о погоде----")
print(f"всего записей {count}")
print(f"средняя температура: {avg_t:.2f} C")
print(f"минимальная температура: {min_t} C")
print(f"максмальная температура: {max_t} C")




conn.close()