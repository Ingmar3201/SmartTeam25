import random

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