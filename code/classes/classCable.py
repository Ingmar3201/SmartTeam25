#from classBattery import Battery
#from classHouse import House

class Cable():
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery
        self.x = [house.x, battery.x, battery.x]
        self.y = [house.y, house.y, battery.y]

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