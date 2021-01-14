class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
        self.connected = False
        self.battery = False
    
    def addCable(self, cable):
        self.cable = cable
        return True
    
    def addBattery(self, battery):
        if self.connected:
            return False

        self.battery = battery
        self.connected = True
        return True
    
    def removeBattery(self):
        if self.connected:
            self.battery = False
            self.cable = False
            self.connected = False
            return True
        
        return False
    
    def getBattery(self):
        if self.connected:
            return self.battery
        
        return False

