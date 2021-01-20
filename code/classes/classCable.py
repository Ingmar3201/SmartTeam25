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
        
        self.makeLocation()


    def calcLength(self):
        length = abs(self.house.x - self.battery.x) + abs(self.house.y - self.battery.y)
        return length

    
    def makeLocation(self):
        self.locations = []
        location = ""
        for i in range(len(self.x)):
            location = f"{self.x[i]},{self.y[i]}"
            self.locations.append(location)