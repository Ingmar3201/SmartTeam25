from classHouse import House

class Battery():
    def __init__(self, position, capacity):
        self._position = position
        self.capacity = float(capacity)
        self._housesDict = {}
        self._totalOutput = 0
        self.id = 0

    def extractCoordinates(self):
        self.x = 0
        self.y = 0
        temp = ""

        for letter in self._position:
            if letter == ",":
                self.x = int(temp)
                temp = ""
            else:
                temp += letter
        self.y = int(temp)
    
    def addHouse(self, house):
        self._totalOutput += house.output
        self._housesDict[house] = abs(house.x - self.x) + abs(house.y - self.y)
        return True


