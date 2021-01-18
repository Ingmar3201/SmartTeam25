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
from classGrid import Grid
from readBattery import readBattery
from readHouse import readHouse
from vis import plot
from classCable import Cable
from bubblesort import bubblesort
from bubblesortBattery import bubblesortBattery
from classObjective import Objective
from initialSolution2 import initialSolution2
from randomSwap2 import randomSwap2

district = 1
runtime = 60 * 0.001

grid = initialSolution2(district)

startPrice = grid.totalCost()

for battery in grid.batteries:
    print(battery.remainingCapacity())

print(f"initial price: {startPrice}")
print(f"total cables {len(grid.cables)}")
print("___________________________")


#reps, bestPrice, bestGrid = randomSwap2(runtime, grid)

#print("___________________________")
#print(f"reps: {reps}")
#print(f"best price: {bestPrice}")

#plot district
#plot(housePath, batteryPath, cables, len(cables))

print("___________________________")

grid.output()
grid.makePlot()



