import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator)

def plot(grid, filename, title):
    '''
    Plots all houses batteries and cables and takes path to housedata batterydata and a list with cable objects
    Gets data from objects and plots houses, batteries and cables
    '''
    # get district data
    houses = grid.houses
    batteries = grid.batteries
    cables = grid.cablesList()
    cablesDict = grid.cables
    district = f"District: {grid.district}"
    totalCosts = f"Total cost: {grid.totalCost()}"

    house_x = []
    house_y = []
    bat_x = []
    bat_y = []

    # gets data from house objects and battery objects
    #for house in houses:
    #    house_x.append(int(house.x))
    #    house_y.append(int(house.y))

    #for battery in batteries:
    #    bat_x.append(int(battery.x))
    #    bat_y.append(int(battery.y))
    
    # set plot attributes
    battery_size = 9
    house_size = 8
    fig_size = 8
    cable_width = 2

    # plots single grid with seperate x and y cordslist for houses and batteries
    fig, ax = plt.subplots(1, figsize=(fig_size, fig_size))
    fig.suptitle(f"{district}: {title}")

    # plot house 
    #ax.plot(house_x, house_y, 'p', color = 'blue', label = 'houses', markersize = house_size)
    
    # plot bat
    #ax.plot(bat_x, bat_y, 's', color = 'red', label = 'batteries', markersize = battery_size)
    
    # plot cables and use diffrent colour for each battery
    
    colors = ['orange', 'magenta', 'cyan', 'lime', 'red']
    
    for cable in cables:
        x = cable.x
        y = cable.y
        id = cable.battery.id

        ax.plot(x, y, '-', color = colors[id], label = 'cable', linewidth = cable_width)

    for house in houses:
        x = house.x
        y = house.y
        id = cablesDict[house].battery.id

        ax.plot(x, y, 'p', color = colors[id], label = 'houses', markersize = house_size)

    for battery in batteries:
        x = battery.x
        y = battery.y
        id = battery.id

        ax.plot(x, y, 's', color = "black", label = 'batteries', markersize = battery_size)


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
    plt.savefig(f"plots/district{filename}.png")
    # plt.show()
   
    









