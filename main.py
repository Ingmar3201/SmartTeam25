import os, sys
import random
import time
import copy
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classGrid import Grid
from classInitialSolution import InitialSolution
from classRandomSwap import RandomSwap
from classShare import Share

runtime = 60 * 0.05


for district in range(1,2):
    
    print(f"DISTRICT: {district}")
    grid = 0
    #grid = RandomSwap(int(district))
    grid = Share(int(district))
    grid.addHouses()
    grid.addBatteries()

    grid.runShare()

    #grid.runInitialSolution()
    #grid.output("")
    grid.makePlot()
    #print(grid.totalCost())
    
    #grid.runRandomSwap(runtime)
    print("_________________________________________")

#print(f"last: {grid.totalCost()}")

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