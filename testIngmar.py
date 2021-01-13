#iter = 169704

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
from classObjective import Objective

district = 3

# create path names
housePath = f"data/district_{district}/district-{district}_houses.csv"
batteryPath =  f"data/district_{district}/district-{district}_batteries.csv"

price_list = []
iterations_list = []
iteration = 0

noFit = True

fitIteration = 0

while noFit:
    fitIteration += 1
    # create house- and battery objects and store them in lists
    houses = readHouse(housePath)
    batteries = readBattery(batteryPath)
    cables = []

    random.shuffle(houses)
    
    totalHouseOutput = 0
    totalBatteryCapacity = 0

    for house in houses:
        totalHouseOutput += house.output
        random.shuffle(batteries)

        for battery in batteries:
            if battery.checkHouse(house):
                cable = battery.addHouse(house)
                cables.append(cable)
                break
        
    for battery in batteries:
        totalBatteryCapacity += battery.capacity

    solution = Objective(cables, batteries)
    current_price = solution.totalCost()
    
    noFit = len(cables) != len(houses)

print(f"battery0: {batteries[0].remainingCapacity()}")
print(f"battery1: {batteries[1].remainingCapacity()}")
print(f"battery2: {batteries[2].remainingCapacity()}")
print(f"battery3: {batteries[3].remainingCapacity()}")
print(f"battery4: {batteries[4].remainingCapacity()}")
print()
#print(f"last house output: {house.output}")
print(f"current price: {current_price}")
print(f"total cables: {len(cables)}")
print()
print(f"total house output: {round(totalHouseOutput, 2)}")
print(f"total battery capacity: {round(totalBatteryCapacity,2)}")
print(f"slack: {round(((totalBatteryCapacity - totalHouseOutput)/totalHouseOutput)*100,2)}%")
print()
print(f"amount of iterations: {fitIteration}")

# plot district
plot(housePath, batteryPath, cables, len(cables))