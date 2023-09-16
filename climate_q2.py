import matplotlib.pyplot as plt
import pandas as pd

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
plt.savefig("co2_temp_2.png") 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('your_data.csv')

years = data['year']
temperatures = data['temperature']

plt.figure(figsize=(10, 6))
plt.plot(years, temperatures, marker='o', linestyle='-')
plt.title('Climate Data Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()
