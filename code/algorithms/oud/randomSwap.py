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
from initialSolution import initialSolution

def randomSwap(runtime, houses, batteries, cables, district):
    bestPrice = 70000
    limitPrice = 70000
    reps = 0

    endTime = time.time() + runtime
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
            #print(f"{reps} : {improvedPrice}")
            houses, batteries, cables = initialSolution(district)

        # district 1: min objective: 53188
        # district 2: min objective: 45268
        # district 3: min objective: 42757

    return reps, bestPrice
