import csv

from classBattery import Battery
from classHouse import House
from classCable import Cable

class Grid():
    def __init__(self, district):
        self.district = district
        #self._points = {}
        self.batteries = []
        self.houses = []
        self.cables = {}
    
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

            for row in reader:
                house = House(row[0], row[1], row[2])
                self.houses.append(house)

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
            
            for row in reader:
                battery = Battery(row[0], row[1])
                battery.extractCoordinates()
                self.batteries.append(battery)

        return True

    def makeConnection(self, house, battery):
        # restrict houses to single connection
        if house in self.cables:
            return False
        
        cable = Cable(house, battery)
        self.cables[house] = cable
        battery.totalOutput += house.output
        return True

    def removeConnection(self, house, battery):
        if house in self.cables:
            del self.cables[house]
            battery.totalOutput -= house.output
            return True
        
        return False

    def hasConnection(self, house):
        return house in self.cables

    def makePlot(self):
        pass