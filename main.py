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

# create path names
housePath = "data/district_1/district-1_houses.csv"
batteryPath =  "data/district_1/district-1_batteries.csv"

# create house- and battery objects and store them lists
houses = readHouse(housePath)
batteries = readBattery(batteryPath)

# create test house bat and cable
cables = []
count = 0

for house in houses:
    # random between 1 and 5
    number = random.random() * 4
    number = round(number)
    battery = batteries[int(number)]
    if battery.checkHouse(house):
        cable = battery.addHouse(house)
        #print(f"{count} - {battery.addHouse(house)}")
        cables.append(cable)
        count += 1 
    #cableTest = Cable(houses[i], batteries[int(number)])

# plot district
plot(housePath, batteryPath, cables, count)
