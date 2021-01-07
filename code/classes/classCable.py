from classBattery import Battery
from classHouse import House

class Cable():
    def __init__(self, house, battery):
        self.house = house
        self.battery = battery
    
    def calcLength(self):
        length = abs(self.house.x - self.battery.x) + abs(self.house.y - self.battery.y)
        return length

