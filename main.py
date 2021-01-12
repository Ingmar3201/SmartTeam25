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

# create path names
housePath = "data/district_1/district-1_houses.csv"
batteryPath =  "data/district_1/district-1_batteries.csv"
price_list = []
iterations_list = []
iteration = 0

endTime = time.time() + 60 * 30

while time.time() < endTime:

    print(round(endTime - time.time(),2))
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
    #print(iteration)

    # # plot district
    # plot(housePath, batteryPath, cables, len(cables))

#plt.plot(iterations_list, price_list)
#plt.savefig('lijnPlot.png')

print(iteration)

bins = int(max(iteration/100, 10))

average = round(sum(price_list) / len(price_list), 2)
max_price = max(price_list)
min_price = min(price_list)
plt.hist(price_list, bins = bins)
plt.suptitle("Verdeling van prijzen")
plt.title((f"Maximale prijs: {max_price}; Mininmale prijs: {min_price}; Gemiddelde prijs: {average}"))
plt.xlabel("Prijs van het grid")
plt.ylabel("Frequentie")
plt.savefig('histogram.png')