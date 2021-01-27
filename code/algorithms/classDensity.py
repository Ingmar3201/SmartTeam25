from classInitialSolution import InitialSolution


class Density(InitialSolution):
    '''
    Optimizes initial solution by swapping houses to other batteries
    Batteries are being chosen, based on density of corresponding houses 
    '''
    
    def runDensity(self):
        '''
        Runs algorithm with corresponding methods
        '''

        # get initial solution
        self.runInitialSolution()

        # recall best solution
        bestSolution = self.clone()
        bestLength = 9 * 10 ** 7

        self.currentSumLength = 0

        # run algorithm 30 times
        for i in range(30):
        
            self.currentSumLength = 0

            # limiting parameter
            self.limitModifier = 1 + i * 0.003
            
            # for every battery remove houses far from the main cluster 
            self.freeHouses = []
            self.removeFarHouses()

            # sorts the removed houses from largest output to smallest
            self.freeHouses = self.sortHouses(self.freeHouses)

            # for every battery calculate the center point of the house cluster
            self.clusterPoints = []
            self.getClusterPoints()

            # assign free house to new battery 
            self.assignToCluster()

            # connect all houses that are still free
            while len(self.cables) < 150:
                self.connectLeftovers()
            
            # save best solution
            if self.currentSumLength < bestLength:
                bestLength = self.currentSumLength
                bestSolution = self.clone()

        self.replaceData(bestSolution)


    def removeFarHouses(self):
        '''
        Removes for every battery houses that are located far away and lonely
        '''

        tempHouses = []

        # check all bateries
        for battery in self.batteries:
            housesLengthList = []
            avarageTotalLength = 0
            houses = self.housesPerBattery(battery)

            # check all houses from battery
            for house in houses:

                # get total distance to all other houses
                length = self.getTotalLength(house, houses)

                # save information
                houseInfo = (house, length)
                housesLengthList.append(houseInfo)
                avarageTotalLength += length
            
            # save average total length
            self.currentSumLength += avarageTotalLength
            avarageTotalLength = int(avarageTotalLength/len(houses))
            
            # sort houses based on distance
            housesLengthList = sorted(housesLengthList, key=lambda houseInfo: houseInfo[1])

            # for all houses check distance relative to average distance
            for houseInfo in housesLengthList:
                tempHouses.append(houseInfo[0])

                # remove house from battery if distance exceeds modified average distance
                if houseInfo[1] > avarageTotalLength * self.limitModifier:
                    if self.removeConnection(houseInfo[0]):
                        self.freeHouses.append(houseInfo[0])
        
        # save houses
        self.houses = tempHouses

        return True


    def getClusterPoints(self):
        '''
        Calculates point with highest house density
        '''

        for battery in self.batteries:
            houses = self.housesPerBattery(battery)
            xTotal = 0
            yTotal = 0

            # calculate average x and y coördinate
            for house in houses:
                xTotal += house.x
                yTotal += house.y
            
            # average coördinate is new clusterpoint
            xAverage = round(xTotal/len(houses),0)
            yAverage = round(yTotal/len(houses),0)

            # save calculated clusterpoint
            self.clusterPoints.append((battery, int(xAverage), int(yAverage)))
        
        return True
    

    def assignToCluster(self):
        '''
        Assigns house to new battery, based on nearest clusterpoint
        '''

        for house in self.freeHouses:
            
            # per house sort clusterpoints from near to far
            self.sortClusterPoints(house)
            
            # assign house to new battery if possible and break
            for cluster in self.clusterPoints:
                if self.makeConnection(house, cluster[0]):
                    break
        
        # if house is re-assignd, remove it from freehouses
        for house in self.houses:
            if self.hasConnection(house) and house in self.freeHouses:
                self.freeHouses.remove(house)

   
    def getTotalLength(self, targetHouse, houses):
        '''
        Calculates total length from house to all other houses from battery
        '''

        totalLength = 0
        for house in houses:
            length = abs(house.x - targetHouse.x) + abs(house.y - targetHouse.y)
            totalLength += length
        
        return totalLength

    
    def sortClusterPoints(self, house):
        '''
        Sorts clusterpoints from near to far for certain house
        '''

        unsorted = self.clusterPoints
        sorted = []

        for i in range(len(self.clusterPoints)):
            minClusterPoint = self.clusterPoints[0]

            # assign maximum possible value
            minLength = 50 * 50

            # calculate length for all clusterpoints
            for j in range(len(unsorted)):
                length = abs(house.x - self.clusterPoints[j][1]) + abs(house.y - self.clusterPoints[j][2])
                
                # save minlength if length is shorter
                if length < minLength:
                    minLength = length
                    minClusterPoint = self.clusterPoints[j]

            
            sorted.append(minClusterPoint)
            unsorted.remove(minClusterPoint)

        # save sorted clusterpoints
        self.clusterPoints = sorted

        return True



    