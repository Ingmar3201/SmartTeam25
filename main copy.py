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
runtime = 60 * 1

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

randomSwap = RandomSwap(grid)
bestCables = randomSwap.runAlgorithm(runtime)

print("___________________________")
print(len(bestCables))
print(len(grid.cables))
print("___________________________")

#for house in grid.houses:
    #print(f"grid cables: {grid.cables[house].battery}")
    #print(f"best cables: {bestCables[house].battery}")
    #print(grid.cables[house].battery == bestCables[house].battery)

print("___________________________")

#grid.output()
#grid.makePlot()

