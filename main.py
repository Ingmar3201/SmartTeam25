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

# create path names
district = 1
housePath = f"data/district_{district}/district-{district}_houses.csv"
batteryPath =  f"data/district_{district}/district-{district}_batteries.csv"

price_list = []
iterations_list = []
iteration = 0

# create house- and battery objects and store them in lists
houses = readHouse(housePath)
houses = bubblesort(houses)
batteries = readBattery(batteryPath)
cables = []

for house in houses:
    print(house.output)
    batteries = bubblesortBattery(batteries, house)

    for battery in batteries:
        if battery.checkHouse(house):
            cable = battery.addHouse(house)
            cables.append(cable)
            break

solution = Objective(cables, batteries)
current_price = solution.totalCost()

print(f"battery0: {batteries[0].remainingCapacity()}")
print(f"battery1: {batteries[1].remainingCapacity()}")
print(f"battery2: {batteries[2].remainingCapacity()}")
print(f"battery3: {batteries[3].remainingCapacity()}")
print(f"battery4: {batteries[4].remainingCapacity()}")
print(f"last house output: {house.output}")
print(f"current price: {current_price}")
print(f"total cables {len(cables)}")


# plot district
plot(housePath, batteryPath, cables, len(cables))