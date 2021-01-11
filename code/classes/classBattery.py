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
        self._totalOutput += house.output
        self._housesDict[house] = abs(house.x - self.x) + abs(house.y - self.y)
        house.connected = True
        cable = Cable(house, self)
        house.addCable(cable)
        return cable
    
    def checkHouse(self, house):
        return self._totalOutput + house.output <= self.capacity

    def remainingCapacity(self):
        return self.capacity - self._totalOutput


