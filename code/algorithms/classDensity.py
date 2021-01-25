#from itertools import permutations
import time

from classInitialSolution import InitialSolution

class Density(InitialSolution):
    
    def runDensity(self):
        self.runInitialSolution()
        
        for i in range(50):
            print(i)
            self.limitModifier = 0.8 + i * 0.01
            # remove houses far from the main cluster of houses per battery
            self.freeHouses = []
            self.removeFarHouses()
            
            #print(len(self.cables))
            #print(len(self.freeHouses))

            # sorts the removed houses from largest output to smallest
            self.freeHouses = self.sortHouses(self.freeHouses)

            # calculate the center point of the 5 house clusters
            self.clusterPoints = []
            self.getClusterPoints()

            self.assignToCluster()

            #print()
            #print(len(self.cables))
            #print(len(self.freeHouses))
            #print("____________")

            while len(self.cables) < 150:
                self.connectLeftovers()

            #self.makePlot("test")


    def removeFarHouses(self):
        for battery in self.batteries:
            housesLengthList = []
            avarageTotalLength = 0
            houses = self.housesPerBattery(battery)
            for house in houses:
                length = self.getTotalLength(house, houses)
                houseInfo = (house, length)
                housesLengthList.append(houseInfo)
                avarageTotalLength += length
            
            avarageTotalLength = int(avarageTotalLength/len(houses))
            
            for houseInfo in housesLengthList:
                if houseInfo[1] > avarageTotalLength * self.limitModifier:
                    if self.removeConnection(houseInfo[0]):
                        self.freeHouses.append(houseInfo[0])
            
        return True


    def getClusterPoints(self):
        for battery in self.batteries:
            houses = self.housesPerBattery(battery)
            xTotal = 0
            yTotal = 0
            for house in houses:
                xTotal += house.x
                yTotal += house.y
            
            xAverage = round(xTotal/len(houses),0)
            yAverage = round(yTotal/len(houses),0)
            self.clusterPoints.append((battery, int(xAverage), int(yAverage)))
        
        return True
    

    def assignToCluster(self):
        for house in self.freeHouses:
            
            self.sortClusterPoints(house)
            
            for cluster in self.clusterPoints:
                if self.makeConnection(house, cluster[0]):
                    break

        for house in self.houses:
            if self.hasConnection(house) and house in self.freeHouses:
                self.freeHouses.remove(house)
            

                #for point in self.clusterPoints:
                #distance = abs(house.x - targetHouse.x) + abs(house.y - targetHouse.y)

   
    def getTotalLength(self, targetHouse, houses):
        totalLength = 0
        for house in houses:
            length = abs(house.x - targetHouse.x) + abs(house.y - targetHouse.y)
            totalLength += length
        
        return totalLength


            #print(f"house loc:{house.x}, {house.y}")
            #print(f"battery loc:{battery.x}, {battery.y}")
    
    
    def sortClusterPoints(self, house):
        unsorted = self.clusterPoints
        sorted = []

        for i in range(len(self.clusterPoints)):
            minClusterPoint = self.clusterPoints[0]
            # assign maximum possible value
            minLength = 50 * 50
            for j in range(len(unsorted)):
                length = abs(house.x - self.clusterPoints[j][1]) + abs(house.y - self.clusterPoints[j][2])
                if length < minLength:
                    minLength = length
                    minClusterPoint = self.clusterPoints[j]
            sorted.append(minClusterPoint)
            unsorted.remove(minClusterPoint)
        
        self.clusterPoints = sorted

        return True
    



    