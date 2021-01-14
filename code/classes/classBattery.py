from classHouse import House
from classCable import Cable

class Battery():
    """
    Defines the components of a battery object
    """
    def __init__(self, position, capacity):
        self._position = position
        self.capacity = float(capacity)
        self._housesDict = {}
        self.housesList = []
        self._totalOutput = 0
        self.id = 0

    def extractCoordinates(self):
        """
        The coordinates are given as a singular string
        This method stores them in separate variables
        """
        self.x = -1
        self.y = -1
        temp = ""

        for letter in self._position:
            # everything before the comma belongs to the x-coordinate
            if letter == ",":
                self.x = int(temp)
                temp = ""
            else:
                temp += letter
        # the remaining characters belong to the y-coordinate
        self.y = int(temp)

        # an eqaution to make it possible to validate the coordinates
        return self.x >= 0 and self.y >= 0
    
    def addHouse(self, house):
        """
        Links a house to the battery and adds the house output to the total output
        """
        if house.connected:
            return False
            
        self._totalOutput += house.output
        self._housesDict[house] = abs(house.x - self.x) + abs(house.y - self.y)
        self.housesList.append(house)
        house.addBattery(self)
        cable = Cable(house, self)
        house.addCable(cable)
        return cable

    def removeHouse(self, house):
        if house in self._housesDict:
            self._totalOutput -= house.output
            cable = house.cable
            del self._housesDict[house]
            self.housesList.remove(house)
            house.removeBattery()
            return cable
        
        return False
    
    def checkHouse(self, house):
        return self._totalOutput + house.output <= self.capacity

    def remainingCapacity(self):
        return self.capacity - self._totalOutput

    def calcLength(self, house):
        length = abs(house.x - self.x) + abs(house.y - self.y)
        return length

