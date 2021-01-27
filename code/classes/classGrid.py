import csv
import json
import copy

from classBattery import Battery
from classHouse import House
from classCable import Cable
from vis import plot

class Grid():
    '''
    This is the parrent class of all algorithms and defines the base structure of the grid
    '''
    
    def __init__(self, district):
        self.district = district
        self.batteries = []
        self.houses = []
        self.cables = {}
        self.loadData()


    def loadData(self):
        '''
        Calls both methods for easier access
        '''
        self.addHouses()
        self.addBatteries()

        return True


    def addHouses(self):
        '''
        Reads data from csv file and creates house class per line
        All objects from class house are stored in a list
        '''
        self.houses = []

        # location of the csv house file
        houseData = f"data/district_{self.district}/district-{self.district}_houses.csv"

        with open(houseData, 'r') as file:
            reader = csv.reader(file)
            next(file, None)

            id = 0

            for row in reader:

                # csv row contains: x, y, output
                house = House(row[0], row[1], row[2], id)
                self.houses.append(house)
                id += 1

        return True


    def addBatteries(self):
        '''
        Reads data from csv file and creates battery class per line
        All objects from class battery are stored in a list
        '''
        self.batteries = []

        # location of the csv battery file
        batteryData = f"data/district_{self.district}/district-{self.district}_batteries.csv"
        
        with open(batteryData, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            
            id = 0
            for row in reader:

                # csv row contains: position, capacity
                battery = Battery(row[0], row[1], id)

                # save x and y in separate variables
                battery.extractCoordinates()
                self.batteries.append(battery)
                id += 1

        return True


    def makeConnection(self, house, battery):
        '''
        Make a connection between a house and battery with a cable
        '''

        # restrict houses to single connection
        if house in self.cables:
            return False

        # house can't be added if the output doesn't fit in the remaining capacity
        elif battery.totalOutput + house.output > battery.capacity:
            return False
        
        # creates cable object, dictionairy entry and updates used battery capacity
        cable = Cable(house, battery)
        self.cables[house] = cable
        battery.totalOutput += house.output

        return True


    def removeConnection(self, house):
        '''
        Remove the connection between house and battery by deleting the cable
        '''

        # house key must exist in cables dictionairy
        if house in self.cables:
            battery = self.cables[house].battery
            del self.cables[house]

            # substract the removed house output from the pooled houses output in the battery
            battery.totalOutput -= house.output
            
            return True
        
        return False


    def hasConnection(self, house):
        '''
        Checks if the house has a connection
        '''
        return house in self.cables


    def swap(self, house0, house1):
        '''
        Swap the batteries of 2 houses
        '''

        # both houses must have a cable
        if house0 in self.cables and house1 in self.cables:
            battery0 = self.cables[house0].battery
            battery1 = self.cables[house1].battery

            # check for both batties if the new house output fits in the capacity
            if battery0.totalOutput - house0.output + house1.output > battery0.capacity:
                return False

            if battery1.totalOutput - house1.output + house0.output > battery1.capacity:
                return False
            
            # remove both house cables and add the houses to the other battery
            self.removeConnection(house0)
            self.removeConnection(house1)
            self.makeConnection(house1, battery0)
            self.makeConnection(house0, battery1)

            return True

        return False
    

    def makePlot(self, name, title):
        '''
        Creates a plot of the current configuration
        '''
        name = f"{self.district}_{name}"
        
        # plots are further handled by a function in vis.py in visualisation
        plot(self, name, title)


    def housesPerBattery(self, battery):
        '''
        Returns a list of all houses connected to a given battery
        '''
        housesInBattery = []
        for house in self.houses:

            # the battery connected to the house can be found by it's cable
            if house in self.cables:
                if self.cables[house].battery == battery:
                    housesInBattery.append(house)

        # the list shouldn't be empty
        if len(housesInBattery) != 0:
            return housesInBattery
        
        return False


    def cablesList(self):
        '''
        Makes a list of all the cable objects in the cables dictionairy
        '''
        cablesList = []
        for house in self.houses:
            cablesList.append(self.cables[house])
        
        return cablesList


    def totalCost(self):
        '''
        Calculates the total cost the the battery - cable configuration of this grid
        '''
        segmentCost = 9
        batteryCost = 5000

        cableSum = 0

        # all cable points of all cables are added to a list
        locationsList = self.cableSegmentList()

        # convert to set to filter repeat points
        locations = set(locationsList)
        
        cableSum = len(locations)
        batterySum = len(self.batteries)

        total = cableSum * segmentCost + batterySum * batteryCost
        
        return total
    

    def output(self, name, costType):
        '''
        Generates an output json file of the current grid configuration
        '''

        # header
        output = [{"district":self.district, costType:self.totalCost()}]

        for battery in self.batteries:
            housesInfo = []

            # make list of houses connected to current battery
            houses = self.housesPerBattery(battery)
            for house in houses:
                cableInfo = []
                
                for i in range(len(self.cables[house].x)):
                    cableInfo.append(f"{self.cables[house].x[i]},{self.cables[house].y[i]}")
                
                housesInfo.append({"location":f"{house.x},{house.y}", "output":house.output, "cables":cableInfo})
            
            batteryInfo = {"location":f"{battery.x},{battery.y}", "capacity":battery.capacity, "houses":housesInfo}
            output.append(batteryInfo)
        
        name = f"results/output_dist{self.district}_{name}.json"

        # save the lists and dictionairies as a json file
        with open(name, 'w') as outfile:
            json.dump(output, outfile, indent=3, sort_keys=True)
        
        return True
    

    def clone(self):
        '''
        Make a clone of the current cable configuration with a deepcopy
        '''
        
        # make a list of cable dictionairy
        cablesList = self.cablesList()
        cablesList = copy.deepcopy(cablesList)

        return cablesList
    

    def replaceData(self, cablesList):
        '''
        Overwrite the the current configuration with a cloned cables list
        '''
        self.houses.clear()
        self.batteries.clear()
        self.cables.clear()

        cablesClone = copy.deepcopy(cablesList)

        # build up a new list of batteries and houses with the cable objects
        for cable in cablesClone:
            house = cable.house
            battery = cable.battery

            # build a new cables dictionairy with the right house objects
            self.cables[house] = cable
            self.houses.append(house)

            # only add each battery once to the battery list
            if battery not in self.batteries:
                self.batteries.append(battery)

        return True
    

    def cableSegmentList(self):
        '''
        Makes a list of all points from each cable, repeat points are accepted
        '''
        locationsList = []

        for house in self.houses:

            # all houses must have a corresponding cable
            if house in self.cables:
                cable = self.cables[house]
                for location in cable.locations:
                    locationsList.append(location)
            else:
                return "unassigned house"
        
        return locationsList