import os, sys
import matplotlib.pyplot as plt
import random
import time


directory = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
#sys.path.append(os.path.join(directory, "code", "algorithms"))
#sys.path.append(os.path.join(directory, "code", "visualisation"))

from classInitialSolution import InitialSolution

# per batterij alle kabels af gaan
    # voor een kabel: # zoek vanaf huis tot batterij 
        # punt voor punt, naar bijliggende kabels in de y richting
            # wordt er iets gevonden
                # check of: 
                    # het een huis is, 
                    # of het bij dezelfde batterij hoort
                    # en of de huis niet al is gebruikt
                # neem alle kabel punten over
                # stop als de kabel in de y richting gaat

class Share(InitialSolution):
    
    def runShare(self):
        
        self.verticalSteps = 10

        self.runInitialSolution()
        print(f"initial cost: {self.totalCost()}")
        self.makePlot()
        time.sleep(3)

        self.getHouseLocation()

        print(f"vertical Steps: {self.verticalSteps}")
        print("______________________")

        count = 0
        #for i in range():
        prevCost = -1
        while prevCost != self.totalCost():
            prevCost = self.totalCost()
            self.relayCables()
            print(f"rep: {count}, new cost: {self.totalCost()}")
            self.makePlot()
            count += 1
            time.sleep(1)

        return True


    def relayCables(self):
        for battery in self.batteries:
            houses = self.housesPerBattery(battery)
            blacklistHouses = []
            houses = self.sortHouseDistance(houses)
            for house in houses:
                waypointHouse = False
                cable = self.cables[house]
                previousY = cable.y[0]

                for i in range(len(cable.x)):
                    x = cable.x[i]
                    y = cable.y[i]
                    if previousY != y:
                        break
                    
                    searchLocations = []
                    for j in range(1,self.verticalSteps + 1):
                        searchLocations.append(f"{x},{y+j}")
                        searchLocations.append(f"{x},{y-j}")

                    for location in searchLocations:
                        if location not in self.houseLocations:
                            continue

                        if self.houseLocations[location] in blacklistHouses:
                            continue

                        if self.houseLocations[location] in houses:
                            waypointHouse = self.houseLocations[location]
                            break
                    
                    if waypointHouse != False:
                        self.segmentCopy(house, waypointHouse, i)
                        blacklistHouses.append(house)
                        break


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
        newX = []
        newY = []

        for i in range(sidetrackPoint + 1):
            newX.append(self.cables[originHouse].x[i])
            newY.append(self.cables[originHouse].y[i])

        difference = self.cables[originHouse].y[sidetrackPoint] - self.cables[waypointHouse].y[0]

        if difference > 1:
            for k in range(1,difference):
                newX.append(newX[-1])
                newY.append(newY[-1] - 1)
        elif difference < -1:
            for k in range(1,abs(difference)):
                newX.append(newX[-1])
                newY.append(newY[-1] + 1)

        for x, y in zip(self.cables[waypointHouse].x, self.cables[waypointHouse].y):
            newX.append(x)
            newY.append(y)
        

        self.cables[originHouse].x = newX
        self.cables[originHouse].y = newY

        self.cables[originHouse].makeLocation()

        """
        if abs(difference) > 2:
            print()
            print(f"difference: {difference}")
            print(f"sidetrackPoint: {sidetrackPoint}")
            coordinates = []

            for x, y in zip(newX, newY):
                coordinates.append(f"{x},{y}")

            print(len(newX) == len(newY))
            print(coordinates)
        """

        return True
        
    
    def sortHouseDistance(self, houses):
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