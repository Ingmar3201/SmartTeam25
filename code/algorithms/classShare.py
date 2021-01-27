from classDensity import Density

class Share(Density):
    '''
    Enables cablesharing between houses by searching for houses lying on parallel cables in the x direction 
    '''
    
    def runShare(self):
        '''
        Control flow of share algorithm
        '''

        # get initial solution (density method from classdensity)
        self.runDensity()
        lowestCost = self.totalCost()
        self.verticalSteps = 0
        bestVerticalSteps = 0
        
        # make a copy of the initial solution
        self.initialCables = self.clone()
        bestSolution = self.clone()

        # set limiting parameters
        maxDeteriorations = 5
        deteriorations = 0

        # scan one step further for houses as long as new configuration within limiting parameters
        while deteriorations < maxDeteriorations:
            self.verticalSteps += 1
            
            # use initial solution copy to save time 
            self.replaceData(self.initialCables)

            # get coordinates of the house objects 
            self.getHouseLocation()
        
            # keep relaying cables for as long as it yields a diffrent result 
            rep = 0
            prevCost = -1
            while prevCost != self.totalCost():
                prevCost = self.totalCost()
                self.relayCables()
                rep += 1
            
            # when a better configuration is found save it and reset the limiting parameters
            if self.totalCost() < lowestCost:
                deteriorations = 0
                lowestCost = self.totalCost()
                bestVerticalSteps = self.verticalSteps
                bestSolution = self.clone()

            else:
                deteriorations += 1
            
        # reset configuration to best configuration
        self.replaceData(bestSolution)
 
        return True


    def relayCables(self):
        '''
        merge cables by making connections between parallel cables 
        '''

        # per battery sort houses from furthest to closest to battery
        for battery in self.batteries:
            houses = self.housesPerBattery(battery)
            blacklistHouses = []
            houses = self.sortHouseDistance(houses)

            # per house scan for nearby houses belonging to the same battery
            for house in houses:
                waypointHouse = False
                cable = self.cables[house]
                previousY = cable.y[0]

                # from house walk in x direction along cable towards battery 
                for i in range(len(cable.x)):
                    x = cable.x[i]
                    y = cable.y[i]

                    # stop when cable direction changes from x to y 
                    if previousY != y:
                        break
                    
                    # on each point of the cable scan for given steps in y direction
                    searchLocations = []
                    for j in range(1,self.verticalSteps + 1):
                        searchLocations.append(f"{x},{y+j}")
                        searchLocations.append(f"{x},{y-j}")

                    # check if location is already scanned
                    for location in searchLocations:
                        if location not in self.houseLocations:
                            continue
                        
                        # if searchlocation has a house which is already relayed avoid it
                        if self.houseLocations[location] in blacklistHouses:
                            continue

                        # if searchlocation has a legal house save this houseobject as waypoint
                        if self.houseLocations[location] in houses:
                            waypointHouse = self.houseLocations[location]
                            break
                    
                    # when a legal house is found relay the cable and add the house to the houseblacklist
                    if waypointHouse != False:
                        self.segmentCopy(house, waypointHouse, i)
                        blacklistHouses.append(house)
                        break

        return True 


    def getHouseLocation(self):
        """
        Creates dictionairy with house coordinates as keys and house objects as values
        Makes it possible to iterate on house locations
        """
        self.houseLocations = {}
        for house in self.houses:
            location = f"{house.x},{house.y}"
            self.houseLocations[location] = house
        
        return True


    def segmentCopy(self, originHouse, waypointHouse, sidetrackPoint):
        '''
        Create new cable segment running from the cable relay point to the new house
        '''
        newX = []
        newY = []

        # get starting point of new cable segment 
        for i in range(sidetrackPoint + 1):
            newX.append(self.cables[originHouse].x[i])
            newY.append(self.cables[originHouse].y[i])

        # calculate distance to new house in y direction 
        difference = self.cables[originHouse].y[sidetrackPoint] - self.cables[waypointHouse].y[0]

        # save cable segment going in negative y direction 
        if difference > 1:
            for k in range(1,difference):
                newX.append(newX[-1])
                newY.append(newY[-1] - 1)

        # save cable segment going in positive y direction 
        elif difference < -1:
            for k in range(1,abs(difference)):
                newX.append(newX[-1])
                newY.append(newY[-1] + 1)

        # save final point of new cable segment 
        for x, y in zip(self.cables[waypointHouse].x, self.cables[waypointHouse].y):
            newX.append(x)
            newY.append(y)
        
        # save new cable segment as cable object 
        self.cables[originHouse].x = newX
        self.cables[originHouse].y = newY
        self.cables[originHouse].makeLocation()

        return True
        
    
    def sortHouseDistance(self, houses):
        '''
        Sorts houses from furthest to closest from battery
        '''
        unsorted = houses
        sorted = []

        for i in range(len(houses)):
            maxHouse = houses[0]

            for j in range(len(unsorted)):
                if self.cables[houses[j]].calcLength() >  self.cables[maxHouse].calcLength():
                    maxHouse = houses[j]
    
            sorted.append(maxHouse)
            unsorted.remove(maxHouse)

        return sorted