import os, sys
import csv
import random
from random import randrange

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

# create path names
housePath = "data/district_1/district-1_houses.csv"
batteryPath =  "data/district_1/district-1_batteries.csv"

noFit = True

while noFit:

    # create house- and battery objects and store them in lists
    houses = readHouse(housePath)
    batteries = readBattery(batteryPath)
    cables = []

    random.shuffle(houses)

    for house in houses:
        random.shuffle(batteries)

        for battery in batteries:
            if battery.checkHouse(house):
                cable = battery.addHouse(house)
                cables.append(cable)
                break

    print(f"battery0: {batteries[0].remainingCapacity()}")
    print(f"battery1: {batteries[1].remainingCapacity()}")
    print(f"battery2: {batteries[2].remainingCapacity()}")
    print(f"battery3: {batteries[3].remainingCapacity()}")
    print(f"battery4: {batteries[4].remainingCapacity()}")
    print(f"last house output = {house.output}")
    
    totCableLength = 0
    for cable in cables:
        totCableLength += cable.calcLength()
    
    print(f"total cables {len(cables)}")
    print()
    noFit = len(cables) != len(houses)

# plot district
plot(housePath, batteryPath, cables, len(cables))
