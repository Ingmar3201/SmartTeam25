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

def initialSolution():

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
    
    return houses, batteries, cables, freeHouses


houses, batteries, cables, freeHouses = initialSolution()



# re-assign to fit
index = 0

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
        
solution = Objective(cables, batteries)
initialPrice = solution.totalCost()

# re-assign to improve

# shuffle houses
# take first 2
# swap
# check output < capacity
# total price > border price
#   initial condition
# repeat

bestPrice = initialPrice
limitPrice = 70000

reps = 0
chain = 0
bestChain = 0

endTime = time.time() + 60 * 0.2
prevMinute = 0.0

while time.time() < endTime:
    
    reps += 1
    
    currentMinute = round((endTime - time.time())/60,1)
    if currentMinute != prevMinute:
        prevMinute = currentMinute
        print(f"remaining minutes: {prevMinute}")

    random.shuffle(houses)
    house0 = houses[0]
    house1 = houses[1]

    battery0 = house0.battery
    battery1 = house1.battery
    cable0 = battery0.removeHouse(house0)
    cable1 = battery1.removeHouse(house1)
    cables.remove(cable0)
    cables.remove(cable1)

    if battery0.checkHouse(house1) and battery1.checkHouse(house0):
        cable0 = battery0.addHouse(house1)
        cable1 = battery1.addHouse(house0)
    else:
        cable0 = battery0.addHouse(house0)
        cable1 = battery1.addHouse(house1)
   
    cables.append(cable0)
    cables.append(cable1)

    solution = Objective(cables, batteries)
    improvedPrice = solution.totalCost()

    if improvedPrice < bestPrice:
        bestPrice = improvedPrice

    if improvedPrice > limitPrice:
        print(f"{reps} : {improvedPrice}")
        houses, batteries, cables, freeHouses = initialSolution()

    """
    # plot district
    #plot(housePath, batteryPath, cables, len(cables))
    if len(cables) > 150:
        print(f"battery0: {batteries[0].remainingCapacity()}")
        print(f"battery1: {batteries[1].remainingCapacity()}")
        print(f"battery2: {batteries[2].remainingCapacity()}")
        print(f"battery3: {batteries[3].remainingCapacity()}")
        print(f"battery4: {batteries[4].remainingCapacity()}")
        #print(f"last house output: {house.output}")
        print(f"initial price: {initialPrice}")
        print(f"improved price: {improvedPrice}")
        print(f"total cables {len(cables)}")
        print("____________________________________________")

    """
    # district 1: min objective: 53188
    # district 2: min objective: 45268
    # district 3: min objective: 42757

print(f"reps: {reps}")
print(f"best price: {bestPrice}")
