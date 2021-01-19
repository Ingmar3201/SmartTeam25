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

runtime = 60 * 0.05

"""
grid = RandomSwap(1)
grid.addHouses()
grid.addBatteries()
bestCables, bestBatteries = grid.runRandomSwap(runtime)
"""

for district in range(1,4):
    grid = 0
    grid = RandomSwap(int(district))
    grid.addHouses()
    grid.addBatteries()
    bestCables, bestBatteries = grid.runRandomSwap(runtime)

#print(f"last: {grid.totalCost()}")