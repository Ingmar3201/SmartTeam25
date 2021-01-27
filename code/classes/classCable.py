class Cable():
    """
    Defines the structure of a cable that spans between a battery and a house
    """
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery

        # the cables starting point is the house
        self.x = [self.house.x]
        self.y = [self.house.y]

        # defines the length when a cable is initialy created
        targetLength = self.calcLength()
        xCurrent = self.house.x
        yCurrent = self.house.y
        
        # a cable is created with n steps in x direction and m steps in y direction
        for i in range(self.calcLength()):
            targetLength -= 1
            if abs(xCurrent + 1 - self.battery.x) + abs(yCurrent - self.battery.y) == targetLength:
                xCurrent += 1
            elif abs(xCurrent - 1 - self.battery.x) + abs(yCurrent - self.battery.y) == targetLength:
                xCurrent -= 1
            elif abs(xCurrent - self.battery.x) + abs(yCurrent + 1 - self.battery.y) == targetLength:
                yCurrent += 1
            elif abs(xCurrent - self.battery.x) + abs(yCurrent - 1 - self.battery.y) == targetLength:
                yCurrent -= 1
            
            # these lists contain all the points a cable passes trough
            self.x.append(xCurrent)
            self.y.append(yCurrent)
        
        # make a list of x, y string pairs 
        self.makeLocation()


    def calcLength(self):
        """
        Gives the Manhattan distance between this cables battery and house
        """
        length = abs(self.house.x - self.battery.x) + abs(self.house.y - self.battery.y)

        return length

    
    def makeLocation(self):
        """
        Creates a new list with the x and y coordinates pairs as one string
        """
        self.locations = []
        location = ""

        for i in range(len(self.x)):
            location = f"{self.x[i]},{self.y[i]}"
            self.locations.append(location)