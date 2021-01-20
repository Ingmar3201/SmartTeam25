import os, sys
import random

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

#from bubblesort import bubblesort
#from bubblesortBattery import bubblesortBattery
from classGrid import Grid

class InitialSolution(Grid):

    def runInitialSolution(self):
        self.sortHouses()

        self.startConnect()

        while len(self.cables) < 150:
            self.connectLeftovers()

        return True
        

    def startConnect(self):
        self.freeHouses = []

        for house in self.houses:
            
            self.sortBatteries(house)

            for battery in self.batteries:
                if self.makeConnection(house, battery):
                    break

            if not self.hasConnection(house):
                self.freeHouses.append(house)

        return True
        

    def connectLeftovers(self):
        for battery in self.batteries:
            housesInBattery = self.housesPerBattery(battery)
            house = housesInBattery[-1]
            if self.removeConnection(house):
                self.freeHouses.append(house)

        for i in range(200):
            random.shuffle(self.freeHouses)
            for house in self.freeHouses:
                self.sortBatteries(house)
                for battery in self.batteries:
                    if self.makeConnection(house, battery):
                        break

            if len(self.cables) < 150:
                for house in self.freeHouses:
                    self.removeConnection(house)
            else:
                break
        
        return True


    def sortBatteries(self, house):
        unsorted = self.batteries
        sorted = []

        for i in range(len(self.batteries)):
            minBattery = self.batteries[0]
            for j in range(len(unsorted)):
                if self.batteries[j].calcLength(house) < minBattery.calcLength(house):
                    minBattery = self.batteries[j]
            sorted.append(minBattery)
            unsorted.remove(minBattery)
        
        self.batteries = sorted

        return True


    def sortHouses(self):
        unsorted = self.houses
        sorted = []

        for i in range(len(self.houses)):
            maxHouse = self.houses[0]
            for j in range(len(unsorted)):
                if self.houses[j].output > maxHouse.output:
                    maxHouse = self.houses[j]
            sorted.append(maxHouse)
            unsorted.remove(maxHouse)
        
        self.houses = sorted

        return True