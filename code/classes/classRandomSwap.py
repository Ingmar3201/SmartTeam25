import os, sys
import random
import time
import matplotlib.pyplot as plt
import copy

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
from initialSolution2 import initialSolution2

class randomSwap(initialGrid):

    def __init__(self, district, initialGrid):
        self.grid = initialGrid
        self.initialSolution = initialGrid
        
    def randomSwap(self, runtime):
        bestPrice = self.grid.totalCost()
        limitPrice = bestPrice * 1.2
        reps = 0
        bestGrid = self.grid

        endTime = time.time() + runtime
        prevMinute = 0.0

        while time.time() < endTime:
            reps += 1
            
            currentMinute = round((endTime - time.time())/60,1)
            if currentMinute != prevMinute:
                prevMinute = currentMinute
                print(f"remaining minutes: {prevMinute}")

            random.shuffle(self.grid.houses)
            house0 = self.grid.houses[0]
            house1 = self.grid.houses[1]

            battery0 = self.grid.cables[house0].battery
            battery1 = self.grid.cables[house1].battery
            self.grid.removeConnection(house0)
            self.grid.removeConnection(house1)

            if battery0.checkHouse(house1) and battery1.checkHouse(house0):
                self.grid.makeConnection(house0, battery1)
                self.grid.makeConnection(house1, battery0)
            else:
                self.grid.makeConnection(house0, battery0)
                self.grid.makeConnection(house1, battery1)

            improvedPrice = self.grid.totalCost()

            if improvedPrice < bestPrice:
                bestPrice = improvedPrice
                bestGrid = copy.deepcopy(self.grid)

            if improvedPrice > limitPrice:
                self.grid = self.initialSolution

            # district 1: min objective: 53188
            # district 2: min objective: 45268
            # district 3: min objective: 42757

        return reps, bestPrice, bestGrid
     

    