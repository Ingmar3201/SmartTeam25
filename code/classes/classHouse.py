"""
Class House stores from every house the coordinates and maximum power output
"""

class House:
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
