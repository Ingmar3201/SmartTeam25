import csv
import json
import copy

from classBattery import Battery
from classHouse import House
from classCable import Cable
from vis import plot

class Grid():
    def __init__(self, district):
        self.district = district
        self.batteries = []
        self.houses = []
        self.cables = {}
        self.loadData()

    def loadData(self):
        self.addHouses()
        self.addBatteries()


    def addHouses(self):
        """
        Reads data from csv file and creates house class per line
        All objects from class house are stored in a list
        """
        self.houses = []
        houseData = f"data/district_{self.district}/district-{self.district}_houses.csv"

        with open(houseData, 'r') as file:
            reader = csv.reader(file)
            next(file, None)

            id = 0
            for row in reader:
                house = House(row[0], row[1], row[2], id)
                self.houses.append(house)
                id += 1

        return True


    def addBatteries(self):
        """
        Reads data from csv file and creates battery class per line
        All objects from class battery are stored in a list
        """
        self.batteries = []
        batteryData = f"data/district_{self.district}/district-{self.district}_batteries.csv"
        
        with open(batteryData, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            
            id = 0
            for row in reader:
                battery = Battery(row[0], row[1], id)
                battery.extractCoordinates()
                self.batteries.append(battery)
                id += 1

        return True


    def makeConnection(self, house, battery):
        """
        Adds a cable object to the cables dictionairy
        Recalculates totalOutput of the battery
        """
        # restrict houses to single connection
        if house in self.cables:
            return False
        elif battery.totalOutput + house.output > battery.capacity:
            return False
        
        cable = Cable(house, battery)
        self.cables[house] = cable
        battery.totalOutput += house.output
        return True


    def removeConnection(self, house):
        """
        Removes the cable object from the cables dictionairy
        Recalculates totalOutput of the battery
        """
        if house in self.cables:
            battery = self.cables[house].battery
            del self.cables[house]
            battery.totalOutput -= house.output
            return True
        
        return False


    def hasConnection(self, house):
        """
        Checks if the house has a connection
        """
        return house in self.cables


    def swap(self, house0, house1):
        if house0 in self.cables and house1 in self.cables:
            battery0 = self.cables[house0].battery
            battery1 = self.cables[house1].battery

            if battery0.totalOutput - house0.output + house1.output > battery0.capacity:
                return False

            if battery1.totalOutput - house1.output + house0.output > battery1.capacity:
                return False
            
            self.removeConnection(house0)
            self.removeConnection(house1)
            self.makeConnection(house1, battery0)
            self.makeConnection(house0, battery1)

            return True

        return False
    

    def makePlot(self, name):
        name = f"{self.district}_{name}"
        plot(self, name)


    def housesPerBattery(self, battery):
        """
        Returns a list of all houses connected to a given battery
        """
        housesInBattery = []
        for house in self.houses:
            if house in self.cables:
                if self.cables[house].battery == battery:
                    housesInBattery.append(house)

        if len(housesInBattery) != 0:
            return housesInBattery
        
        return False


    def cablesList(self):
        """
        Makes a list of all the cable objects in the cables dictionairy
        """
        cablesList = []
        for house in self.houses:
            cablesList.append(self.cables[house])
        
        return cablesList


    def totalCost(self):
        """
        Calculates the total cost the the battery - cable configuration of this grid
        """
        segmentCost = 9
        batteryCost = 5000
        cableSum = 0

        locationsList = self.cableSegmentList()
        locations = set(locationsList)
        
        cableSum = len(locations)

        batterySum = len(self.batteries)

        total = cableSum * segmentCost + batterySum * batteryCost
        
        return total
    

    def output(self, name, costType):
        """

        """
        output = [{"district":self.district, costType:self.totalCost()}]
        for battery in self.batteries:
            housesInfo = []
            houses = self.housesPerBattery(battery)
            for house in houses:
                cableInfo = []
                for i in range(len(self.cables[house].x)):
                    cableInfo.append(f"{self.cables[house].x[i]},{self.cables[house].y[i]}")
                housesInfo.append({"location":f"{house.x},{house.y}", "output":house.output, "cables":cableInfo})
            
            batteryInfo = {"location":f"{battery.x},{battery.y}", "capacity":battery.capacity, "houses":housesInfo}
            output.append(batteryInfo)
        
        #now = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        #name = f"results/output_dist{self.district}_{now}.json"
        name = f"results/output_dist{self.district}_{name}.json"

        with open(name, 'w') as outfile:
            json.dump(output, outfile, indent=3, sort_keys=True)
        
        return True
        #return json.dumps(output, indent=3, sort_keys=True)
    

    def clone(self):
        cablesList = self.cablesList()
        cablesList = copy.deepcopy(cablesList)

        return cablesList
    

    def replaceData(self, cablesList):
        self.houses.clear()
        self.batteries.clear()
        self.cables.clear()

        cablesClone = copy.deepcopy(cablesList)

        for cable in cablesClone:
            house = cable.house
            battery = cable.battery
            self.cables[house] = cable
            self.houses.append(house)
            if battery not in self.batteries:
                self.batteries.append(battery)

        return True
    

    def cableSegmentList(self):
        locationsList = []

        for house in self.houses:
            if house in self.cables:
                cable = self.cables[house]
                for location in cable.locations:
                    locationsList.append(location)
            else:
                return "unassigned house"
        
        return locationsList