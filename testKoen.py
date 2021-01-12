import os, sys
import csv
import random
from random import randrange
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

# create path names
housePath = "data/district_1/district-1_houses.csv"
batteryPath =  "data/district_1/district-1_batteries.csv"
price_list = []
iterations_list = []
iteration = 0


for i in range(0, 100):

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

        solution = Objective(cables, batteries)
        current_price = solution.totalCost()
        
        # print(f"battery0: {batteries[0].remainingCapacity()}")
        # print(f"battery1: {batteries[1].remainingCapacity()}")
        # print(f"battery2: {batteries[2].remainingCapacity()}")
        # print(f"battery3: {batteries[3].remainingCapacity()}")
        # print(f"battery4: {batteries[4].remainingCapacity()}")
        # print(f"last house output: {house.output}")
        # print(f"current price: {current_price}")
        # print(f"total cables {len(cables)}")
        
        totCableLength = 0
        for cable in cables:
            totCableLength += cable.calcLength()
        
        noFit = len(cables) != len(houses)
        
    iteration += 1
    iterations_list.append(iteration)
    price_list.append(current_price)
    print(iteration)

    # # plot district
    # plot(housePath, batteryPath, cables, len(cables))


plt.hist(price_list, bins = 100)
plt.show()
