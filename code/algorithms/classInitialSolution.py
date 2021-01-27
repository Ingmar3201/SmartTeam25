import random
from classGrid import Grid


class InitialSolution(Grid):
    '''
    Creates initial solution by connecting all houses to batteries without exceeding max capacity
    '''

    def runInitialSolution(self):
        '''
        Controls flow of algorithm
        '''
        self.cables = {}

        # get house and battery objects (method in class grid)
        self.loadData()

        # sort houses based on output 
        self.houses = self.sortHouses(self.houses)       

        # start connecting houses based on output and distance  
        self.startConnect()

        # keep trying to connect unconnected houses until all houses are connected
        while len(self.cables) < 150:
            self.connectLeftovers()

        return True
        
    
    def startConnect(self):
        '''
        Connects all houses from largest to smallest output to closest battery and saves remaining houses 
        '''
        self.freeHouses = []

        for house in self.houses:
            
            # sort batteries from smallest to largest distance to given house 
            self.sortBatteries(house)

            # try to make connection if possible (method in class grid)
            for battery in self.batteries:
                if self.makeConnection(house, battery):
                    break

            # add house to leftover houses if impossible to connect (method in class grid)
            if not self.hasConnection(house):
                self.freeHouses.append(house)

        return True
        

    def connectLeftovers(self):
        '''
        Try to connect leftover houses by making room in the batteries and trying again 
        '''

        # remove house with lowest output from battery to make room and add to lefover houses
        for battery in self.batteries:
            housesInBattery = self.housesPerBattery(battery)
            smallest_house = housesInBattery[-1]

            if self.removeConnection(smallest_house):
                self.freeHouses.append(smallest_house)

        # try to reconnect random lefover houses multiple times or until all houses are connected
        for i in range(200):
            random.shuffle(self.freeHouses)

            # try to connect all freehouses to closest battery
            for house in self.freeHouses:
                self.sortBatteries(house)

                for battery in self.batteries:                        
                    if self.makeConnection(house, battery):
                        break
            
            # if unsuccesfull reset freehouses 
            if len(self.cables) < 150:
                for house in self.freeHouses:
                    self.removeConnection(house)
            else:
                break
        
        return True


    def sortBatteries(self, house):
        '''
        Sorts batteries from largest to smallest distance to a given house
        '''
        unsorted = self.batteries
        sorted = []

        for i in range(len(self.batteries)):
            minBattery = self.batteries[0]

            # determine battery closest to house and save 
            for j in range(len(unsorted)):
                if self.batteries[j].calcLength(house) < minBattery.calcLength(house):
                    minBattery = self.batteries[j]

            sorted.append(minBattery)
            unsorted.remove(minBattery)
        
        self.batteries = sorted

        return True


    def sortHouses(self, houses):
        '''
        Sort houses from largest output to smallest output 
        '''
        unsorted = houses
        sorted = []

        for i in range(len(houses)):
            maxHouse = houses[0]

            # determine house with largest output and save
            for j in range(len(unsorted)):
                if houses[j].output > maxHouse.output:
                    maxHouse = houses[j]
            
            sorted.append(maxHouse)
            unsorted.remove(maxHouse)

        return sorted