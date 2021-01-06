import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

from classHouse import House 
from classBattery import CBattery
from dataReader import houses
from dataReader import batteries


house_x = []
house_y = []
bat_x = []
bat_y = []


# get data
for house in houses:
    house_x.append(int(house.x))
    house_y.append(int(house.y))

for battery in batteries:
    bat_x.append(int(battery.x))
    bat_y.append(int(battery.y))


# plot district
fig, ax = plt.subplots(1, figsize=(10, 10))
fig.suptitle('District 1')

ax.plot(house_x, house_y, 'o', color = 'blue', label = 'houses', markersize = 7)
ax.legend()
ax.plot(bat_x, bat_y, 'o', color = 'red', label = 'batteries', markersize = 7)
ax.legend()

ax.xaxis.set_minor_locator(AutoMinorLocator(10))
ax.yaxis.set_minor_locator(AutoMinorLocator(10))

plt.xlim(-1, 51)
plt.ylim(-1, 51)

plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='black', linestyle='-', alpha = 0.2)

plt.show()



