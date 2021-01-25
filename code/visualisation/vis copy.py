'''
Gets data from objects and plots houses, batteries and cables
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))


#from readBattery import readBattery
#from readHouse import readHouse
#from classCable import Cable 
#from objective import objective


def plot(grid, name):
    '''
    Plots all houses batteries and cables and takes path to housedata batterydata and a list with cable objects
    '''
    # get district data
    houses = grid.houses
    batteries = grid.batteries
    cables = grid.cablesList()
    district = f"District: {grid.district}"
    totalCosts = f"Total cost: {grid.totalCost()}"

    house_x = []
    house_y = []
    bat_x = []
    bat_y = []

    # gets data from house objects and battery objects
    for house in houses:
        house_x.append(int(house.x))
        house_y.append(int(house.y))

    for battery in batteries:
        bat_x.append(int(battery.x))
        bat_y.append(int(battery.y))
    
    # set plot attributes
    battery_size = 9
    house_size = 14
    fig_size = 8
    cable_width = 2

    # plots single grid with seperate x and y cordslist for houses and batteries
    fig, ax = plt.subplots(1, figsize=(fig_size, fig_size))
    fig.suptitle(district)

    # plot house 
    ax.plot(house_x, house_y, 'p', color = 'blue', label = 'houses', markersize = house_size)
    
    # plot bat
    ax.plot(bat_x, bat_y, 's', color = 'red', label = 'batteries', markersize = battery_size)
    
    # plot cables and use diffrent colour for each battery
    for cable in cables:
        x = cable.x
        y = cable.y

        if cable.battery.id == 0:
            ax.plot(x, y, '-', color = 'orange', label = 'cable', linewidth = cable_width)

        elif cable.battery.id == 1:
            ax.plot(x, y, '-', color = 'purple', label = 'cable', linewidth = cable_width)
        
        elif cable.battery.id == 2:
            ax.plot(x, y, '-', color = 'c', label = 'cable', linewidth = cable_width)

        elif cable.battery.id == 3:
            ax.plot(x, y, '-', color = 'green', label = 'cable', linewidth = cable_width)

        elif cable.battery.id == 4:
            ax.plot(x, y, '-', color = 'pink', label = 'cable', linewidth = cable_width)


    # plot grid
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
  
    plt.xlim(-1, 51)
    plt.ylim(-1, 51)

    # show visualisaton
    plt.grid(b=True, which='major', color='black', linestyle='-')
    plt.grid(b=True, which='minor', color='black', linestyle='-', alpha = 0.2)
    plt.title(totalCosts)
    plt.suptitle(district)
    plt.savefig(f"plots/district{name}.png")
    # plt.show()
   
    








