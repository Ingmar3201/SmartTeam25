import os, sys
import csv
import random

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

    # create house- and battery objects and store them lists
    houses = readHouse(housePath)
    houses = bubblesort(houses)

    batteries = readBattery(batteryPath)

    # create test house bat and cable
    cables = []
    count = 0

    for house in houses:
        # random between 0 and 4
        battery = batteries[int(round(random.random() * 4))]
        
        quitCount = 10

        while not battery.checkHouse(house) and quitCount > 0:
            battery = batteries[int(round(random.random() * 4))]
            quitCount -= 1

        if battery.checkHouse(house):      
            cable = battery.addHouse(house)
            #print(f"{count} - {battery.addHouse(house)}")
            cables.append(cable)
            count += 1

    print(f"battery0: {batteries[0].remainingCapacity()}")
    print(f"battery1: {batteries[1].remainingCapacity()}")
    print(f"battery2: {batteries[2].remainingCapacity()}")
    print(f"battery3: {batteries[3].remainingCapacity()}")
    print(f"battery4: {batteries[4].remainingCapacity()}")

    print(len(cables))
    noFit = len(cables) != len(houses)
    print(noFit)


# plot district
plot(housePath, batteryPath, cables, count)
