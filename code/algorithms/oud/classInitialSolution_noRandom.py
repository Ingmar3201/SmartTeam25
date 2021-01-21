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

        self.allConnected = False
        #while len(self.cables) < 150:
        while not self.allConnected:
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
        baseRemainingBatteryCapacity = {}
        for battery in self.batteries:
            housesInBattery = self.housesPerBattery(battery)
            house = housesInBattery[-1]
            
            if self.removeConnection(house):
                self.freeHouses.append(house)
            
            baseRemainingBatteryCapacity[battery] = battery.remainingCapacity()
            #print(remainingBatteryCapacity[battery])

        #permutationsList = [(0, 1, 3, 4, 6, 7, 8, 10, 2, 5, 9)]
        n = len(self.freeHouses)
        
        #perms = list(permutations(range(n), n))
        #perms = [perms[0], perms[1]]

        for attempt in permutations(range(n), n):
        #for attempt in perms:
            #currentRemainingBatteryCapacity= copy.deepcopy(baseRemainingBatteryCapacity)
            #print(attempt)
            currentRemainingBatteryCapacity = {}

            for battery in self.batteries:
                currentRemainingBatteryCapacity[battery] = baseRemainingBatteryCapacity[battery]

            self.freeHouses = self.sortHouses(self.freeHouses)     
            
            temp = []
            for j in attempt:
                temp.append(self.freeHouses[j])
            
            self.freeHouses = temp
            
            amountToConnect = n

            #random.shuffle(self.freeHouses)
            for house in self.freeHouses:
                self.sortBatteries(house)
                for battery in self.batteries:
                    if currentRemainingBatteryCapacity[battery] - house.output > 0:
                        currentRemainingBatteryCapacity[battery] -= house.output
                        amountToConnect -= 1
                        break
                    #if self.makeConnection(house, battery):
            
            #if len(self.cables) < 150:
            if amountToConnect == 0:
                print(attempt)
                self.allConnected = True
                for house in self.freeHouses:
                    self.sortBatteries(house)
                    for battery in self.batteries:
                        if self.makeConnection(house, battery):
                            break
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