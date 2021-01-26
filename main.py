import os, sys
import random
import time
import copy
import matplotlib.pyplot as plt
import datetime

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classGrid import Grid
from classInitialSolution import InitialSolution
#from classRandomSwap import RandomSwap
from classShare import Share
from classDensity import Density


startTime = time.time()
prevMinute = 0.0

theBestGrids = []
nonFeasible = 0

for district in range(1,4):
    print("_______________________")
    print("District:", district)
    print("_______________________")
    grids = []
    iterations = 0
    while len(grids) < 101:
        print("Iteration:", iterations)
        currentMinute = round((time.time() - startTime)/60,1)
        if currentMinute != prevMinute:
            prevMinute = currentMinute
            print(f"Runtime: {prevMinute} minutes")
        try:
            grid = Share(int(district))
            grid.runShare()
            grids.append(grid)
        except TypeError:
            nonFeasible += 1

        iterations += 1

    bestGrid = grids[0]
    bestCost = grids[0].totalCost()

    for grid in grids:
        cost = grid.totalCost()
        if cost < bestCost:
            bestCost = cost
            bestGrid = grid
    
    theBestGrids.append(bestGrid)

for grid in theBestGrids:
    grid.makePlot("theBest")


print("amount of non-feasible solutions", nonFeasible)
        

    




"""
DISTRICT: 1
36547
_________________________________________
DISTRICT: 2
35890
_________________________________________
DISTRICT: 3
35467
"""