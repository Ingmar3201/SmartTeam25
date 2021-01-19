import os, sys
import random

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from bubblesort import bubblesort
from bubblesortBattery import bubblesortBattery
#from classGrid import Grid

class InitialSolution():
    def __init__(self, grid):
        self.grid = grid
        self.grid.houses = bubblesort(self.grid.houses)


    def start(self):
        self.freeHouses = []
        for house in self.grid.houses:
            self.grid.batteries = bubblesortBattery(self.grid.batteries, house)

            for battery in self.grid.batteries:
                if self.grid.makeConnection(house, battery):
                    break

            if not self.grid.hasConnection(house):
                self.freeHouses.append(house)
        

    def connectAll(self):
        for battery in self.grid.batteries:
            housesInBattery = self.grid.housesPerBattery(battery)
            house = housesInBattery[-1]
            if self.grid.removeConnection(house):
                self.freeHouses.append(house)

        for i in range(200):
            random.shuffle(self.freeHouses)
            for house in self.freeHouses:
                self.grid.batteries = bubblesortBattery(self.grid.batteries, house)
                for battery in self.grid.batteries:
                    if self.grid.makeConnection(house, battery):
                        break

            if len(self.grid.cables) < 150:
                for house in self.freeHouses:
                    self.grid.removeConnection(house)
            else:
                break


    def runAlgorithm(self):
        self.start()

        while len(self.grid.cables) < 150:
            self.connectAll()

        return True