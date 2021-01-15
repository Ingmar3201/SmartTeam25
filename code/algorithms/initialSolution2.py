import os, sys
import random
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

#from readBattery import readBattery
#from readHouse import readHouse
from classGrid import Grid
from vis import plot
from bubblesort import bubblesort
from bubblesortBattery import bubblesortBattery


def initialSolution2(district):

    # create path names
    grid = Grid(district)
    # create house- and battery objects and store them in lists
    grid.addHouses()
    grid.addBatteries()
    grid.houses = bubblesort(grid.houses)
    freeHouses = []

    

    # start solution
    for house in grid.houses:
        # print(house.output)
        grid.batteries = bubblesortBattery(grid.batteries, house)

        for battery in grid.batteries:
            if battery.checkHouse(house):
                grid.makeConnection(house, battery)
                break

        if not grid.hasConnection(house):
            freeHouses.append(house)
    
    # re-assign leftover houses
    while len(grid.cables) < 150:

        for battery in grid.batteries:
            housesInBattery = bubblesort(grid.housesPerBattery(battery))
            house = housesInBattery[-1]
            grid.removeConnection(house)
            freeHouses.append(house)

        for i in range(200):
            random.shuffle(freeHouses)
            for house in freeHouses:
                grid.batteries = bubblesortBattery(grid.batteries, house)
                for battery in grid.batteries:
                    if battery.checkHouse(house):
                        grid.makeConnection(house, battery)
                        break

            if len(grid.cables) < 150:
                for house in freeHouses:
                    if grid.hasConnection(house):
                        grid.removeConnection(house)
            else:
                print(f"i: {i}")
                print(f"amount freeHouses: {len(freeHouses)}")
                break
        
    return grid