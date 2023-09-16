import matplotlib.pyplot as plt
years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
import sqlite3
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
years = []
temp = []
cursor.execute("SELECT year, temperature FROM climate_data ORDER BY year")
data = cursor.fetchall()
for row in data:
    years.append(row[0])
    temp.append(row[1])

conn.close()


