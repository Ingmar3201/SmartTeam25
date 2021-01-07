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
from classCable import Cable 

def plot(path_houses, path_batteries, cables_list):
    batteries = readBattery(path_batteries)
    houses = readHouse(path_houses)

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
    fig_size = 6

    fig, ax = plt.subplots(1, figsize=(fig_size, fig_size))
    fig.suptitle('District 1')

    # plot house 
    ax.plot(house_x, house_y, 'p', color = 'blue', label = 'houses', markersize = icon_size)
    

    # plot bat
    ax.plot(bat_x, bat_y, 's', color = 'red', label = 'batteries', markersize = icon_size)
    

    # plot cable 
    for cable in cables_list:
        x = cable.x
        y = cable.y

        ax.plot(x, y, '-', color = 'yellow', label = 'cable')
    

    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))

    plt.xlim(-1, 51)
    plt.ylim(-1, 51)

    plt.grid(b=True, which='major', color='black', linestyle='-')
    plt.grid(b=True, which='minor', color='black', linestyle='-', alpha = 0.2)
    #ax.legend()
    plt.show()








