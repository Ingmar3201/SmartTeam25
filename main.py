import os, sys
import random
import time
import matplotlib.pyplot as plt


directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classGrid import Grid
from classInitialSolution import InitialSolution
from classRandomSwap import RandomSwap

district = 1
runtime = 60 * 0.01

grid = Grid(district)
grid.addHouses()
grid.addBatteries()

initial = InitialSolution(grid)
initial.runAlgorithm()


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

#grid.output()
#grid.makePlot()



