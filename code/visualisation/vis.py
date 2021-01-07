# By Koen Smallegange 
# For programmeertheorie - SmartTeam25
# Splits data from dataReader.py and plots houses and batteries for 1 district

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from readBattery import readBattery
from readHouse import readHouse


def plot():
    batteries = readBattery("data/district_1/district-1_batteries.csv")
    houses = readHouse("data/district_1/district-1_houses.csv")

    house_x = []
    house_y = []
    bat_x = []
    bat_y = []

    # gets data from dataReader.py

    for house in houses:
        house_x.append(int(house.x))
        house_y.append(int(house.y))

    for battery in batteries:
        bat_x.append(int(battery.x))
        bat_y.append(int(battery.y))
    
    # plots single grid with seperate x and y cordslist for houses and batteries
    icon_size = 9

    fig, ax = plt.subplots(1, figsize=(10, 10))
    fig.suptitle('District 1')

    ax.plot(house_x, house_y, 'p', color = 'blue', label = 'houses', markersize = icon_size)
    ax.legend()
    ax.plot(bat_x, bat_y, 's', color = 'red', label = 'batteries', markersize = icon_size)
    ax.legend()

    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))

    plt.xlim(-1, 51)
    plt.ylim(-1, 51)

    plt.grid(b=True, which='major', color='black', linestyle='-')
    plt.grid(b=True, which='minor', color='black', linestyle='-', alpha = 0.2)

    plt.show()








