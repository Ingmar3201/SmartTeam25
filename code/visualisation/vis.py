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


from readBattery import readBattery
from readHouse import readHouse
from classCable import Cable 
from objective import objective



def plot(path_houses, path_batteries, cables_list, count):
    '''
    Plots all houses batteries and cables and takes path to housedata batterydata and a list with cable objects
    '''
    # get list with house objects and battery objects
    batteries = readBattery(path_batteries)
    houses = readHouse(path_houses)

    house_x = []
    house_y = []
    bat_x = []
    bat_y = []

    # get total cost
    total_costs = objective(cables_list, batteries)

    # gets data from house objects and battery objects
    for house in houses:
        house_x.append(int(house.x))
        house_y.append(int(house.y))

    for battery in batteries:
        bat_x.append(int(battery.x))
        bat_y.append(int(battery.y))
    
    battery_size = 9
    house_size = 14
    fig_size = 12
    cable_width = 2

    # plots single grid with seperate x and y cordslist for houses and batteries
    fig, ax = plt.subplots(1, figsize=(fig_size, fig_size))
    fig.suptitle('District 1')

    # plot house 
    ax.plot(house_x, house_y, 'p', color = 'blue', label = 'houses', markersize = house_size)
    
    # plot bat
    ax.plot(bat_x, bat_y, 's', color = 'red', label = 'batteries', markersize = battery_size)
    
    # plot cables and use diffrent colour for each battery
    for cable in cables_list:
        x = cable.x
        y = cable.y

        if cable.battery.id == 0:
            ax.plot(x, y, '-', color = 'yellow', label = 'cable', linewidth = cable_width)
        
        elif cable.battery.id == 1:
            ax.plot(x, y, '-', color = 'purple', label = 'cable', linewidth = cable_width)
        
        elif cable.battery.id == 2:
            ax.plot(x, y, '-', color = 'orange', label = 'cable', linewidth = cable_width)

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
    plt.title(total_costs)
    plt.suptitle(count)
    plt.savefig('plotje.png')
    # plt.show()
   
    









