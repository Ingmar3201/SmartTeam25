class Cable():
    def __init__(house, battery):
        self.house = house
        self.battery = battery
        self.length = 0
        self._segment_cost = 9
        self.total_cost = 0
        
    def cable_cost(self):
        self.total_cost = self.length * self._segment_cost
        return self.total_cost
    
    def calc_length(self):
        self.length = abs(self.house.x − self.battery.x) + abs(self.house.y − self.battery.y)
        return self.length

