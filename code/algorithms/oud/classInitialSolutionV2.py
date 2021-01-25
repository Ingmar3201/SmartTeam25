import os, sys
import random
from itertools import permutations
import copy

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

        self.cables = {}
        self.loadData()

        self.houses = self.sortHouses(self.houses)

        self.startConnect()

        while len(self.cables) < 150:
            self.connectLeftovers()
        
        return True     
    

    def startConnect(self):
        self.freeHouses = []

        for house in self.houses:
            x = house.x
            
            place = [0, 1, 2, 3, 4]

            if x < 10:
                place = [0, 1, 2, 3, 4]
            elif x < 20:
                place = [1, 0, 2, 3, 4]
            elif x < 30:
                place = [2, 1, 3, 0, 4]
            elif x < 40:
                place = [3, 2, 4, 1, 0]
            elif x < 51:
                place = [4, 3, 2, 1, 0]
            
            #self.sortBatteries(house)

            for id in place:
                battery = 0
                for bat in self.batteries:
                    if bat.id == id:
                        battery = bat
                        break

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


    def sortHouses(self, houses):
        unsorted = houses
        sorted = []

        for i in range(len(houses)):
            maxHouse = houses[0]
            for j in range(len(unsorted)):
                if houses[j].output > maxHouse.output:
                    maxHouse = houses[j]
            sorted.append(maxHouse)
            unsorted.remove(maxHouse)

        return sorted

