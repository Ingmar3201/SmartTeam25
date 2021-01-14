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
from randomSwap import randomSwap

district = 1

houses, batteries, cables = initialSolution(district)

solution = Objective(cables, batteries)
initialPrice = solution.totalCost()

print(f"initial price: {initialPrice}")
print(f"total cables {len(cables)}")
print("___________________________")

reps, bestPrice = randomSwap(60 * 0.20, houses, batteries, cables, district)

solution = Objective(cables, batteries)
improvedPrice = solution.totalCost()

print("___________________________")
print(f"reps: {reps}")
print(f"best price: {bestPrice}")

#plot district
#plot(housePath, batteryPath, cables, len(cables))