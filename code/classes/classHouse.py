class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
        self.connected = False
    
    def addCable(self, cable):
        self.cable = cable
        return True
