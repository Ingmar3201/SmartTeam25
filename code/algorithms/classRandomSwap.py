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
from classGrid import Grid
from readBattery import readBattery
from readHouse import readHouse
from vis import plot
from classCable import Cable
from bubblesort import bubblesort
from bubblesortBattery import bubblesortBattery
from classObjective import Objective
from classInitialSolution import InitialSolution


class RandomSwap():

    def __init__(self, grid):
        self.grid = grid
        #houses, batteries, cables = self.grid.clone()
        #self.initialGrid = Grid(self.grid.district)
        #self.initialGrid.houses = houses
        #self.initialGrid.batteries = batteries
        #self.initialGrid.cables = cables


    def runAlgorithm(self, runtime):
        self.randomSwap(runtime)

        return self.bestPrice


    def randomSwap(self, runtime):
        bestPrice = self.grid.totalCost()
        limitPrice = bestPrice * 1.2
        reps = 0
        #self.bestGrid = self.grid
        self.bestPrice = limitPrice
        
        #self.bestGrid = self.initialGrid

        endTime = time.time() + runtime
        prevMinute = 0.0

        while time.time() < endTime:
            reps += 1
            #print(reps)
        
            currentMinute = round((endTime - time.time())/60,1)
            if currentMinute != prevMinute:
                prevMinute = currentMinute
                print(f"remaining minutes: {prevMinute}")

            random.shuffle(self.grid.houses)
            house0 = self.grid.houses[0]
            house1 = self.grid.houses[1]
            self.grid.swap(house0, house1)
            
            #count = 0
            #for house in self.grid.houses:
             #   count += 1
                #print(house.output, count)
                #print(count, self.grid.cables[house])
            
            improvedPrice = self.grid.totalCost()

            if improvedPrice < self.bestPrice:
                self.bestPrice = improvedPrice
                #houses, batteries, cables = self.grid.clone()
                #self.bestGrid = Grid(self.grid.district)
                #self.bestGrid.houses = houses
                #self.bestGrid.batteries = batteries
                #self.bestGrid.cables = cables
                

            if improvedPrice > limitPrice:
                self.grid = Grid(self.grid.district)
                self.grid.addHouses()
                self.grid.addBatteries()
                initial = InitialSolution(self.grid)
                initial.runAlgorithm()
                #print("succes")

            # district 1: min objective: 53188
            # district 2: min objective: 45268
            # district 3: min objective: 42757

        return True
     

    