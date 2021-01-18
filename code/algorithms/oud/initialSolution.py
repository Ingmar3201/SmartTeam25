import os, sys
import random
import time
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classBattery import Battery
from classHouse import House
from readBattery import readBattery
from readHouse import readHouse
from vis import plot
from classCable import Cable
from bubblesort import bubblesort
from bubblesortBattery import bubblesortBattery
from classObjective import Objective



def initialSolution(district):

    # create path names
    housePath = f"data/district_{district}/district-{district}_houses.csv"
    batteryPath =  f"data/district_{district}/district-{district}_batteries.csv"

    # create house- and battery objects and store them in lists
    houses = readHouse(housePath)
    houses = bubblesort(houses)
    batteries = readBattery(batteryPath)
    cables = []
    freeHouses = []

    # start solution
    for house in houses:
        # print(house.output)
        batteries = bubblesortBattery(batteries, house)

        for battery in batteries:
            if battery.checkHouse(house):
                cable = battery.addHouse(house)
                cables.append(cable)
                break

        if not house.connected:
            freeHouses.append(house)
    
    # re-assign leftover houses
    while len(cables) < 150:

        for battery in batteries:
            house = battery.housesList[-1]
            cable = battery.removeHouse(house)
            cables.remove(cable)
            freeHouses.append(house)

        for i in range(200):
            random.shuffle(freeHouses)
            for house in freeHouses:
                #print(house.output)
                batteries = bubblesortBattery(batteries, house)
                #random.shuffle(batteries)

                for battery in batteries:
                    if battery.checkHouse(house):
                        cable = battery.addHouse(house)
                        cables.append(cable)
                        break

            if len(cables) < 150:
                for house in freeHouses:
                    # print(house.output)
                    if house.connected:
                        battery = house.battery
                        cable = battery.removeHouse(house)
                        cables.remove(cable)
            else:
                print(f"i: {i}")
                print(f"amount freeHouses: {len(freeHouses)}")
                break
        
    return houses, batteries, cables