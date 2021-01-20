#from classBattery import Battery
#from classHouse import House

class Cable():
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery
        self.x = [self.house.x]
        self.y = [self.house.y]

        targetLength = self.calcLength()
        xCurrent = self.house.x
        yCurrent = self.house.y
        
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

            self.x.append(xCurrent)
            self.y.append(yCurrent)

        """
        if self.house.x < self.battery.x:
            xLeft = self.house.x
            xRight = self.battery.x + 1
        else:
            xLeft = self.battery.x
            xRight = self.house.x + 1

        for x in range(xLeft, xRight):
            self.x.append(x)
        
        """
        #self.x = [house.x, battery.x, battery.x]
        #self.y = [house.y, house.y, battery.y]

    def calcLength(self):
        length = abs(self.house.x - self.battery.x) + abs(self.house.y - self.battery.y)
        return length

"""
    def createRoute(self):
        start = (self.house.x, self.house.y)
        corner = (self.battery.x , self.house.y)
        end = (self.battery.x, self.battery.y)
        self.route = [start, corner, end]
        return self.route
 """