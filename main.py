import os, sys
import csv

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
testBat = batteries[0]
testHouse = houses[0]
cableTest = Cable(testHouse, testBat)

# store cable object in cablelist
cables = []
cables.append(cableTest)

# plot district
plot(housePath, batteryPath, cables)
