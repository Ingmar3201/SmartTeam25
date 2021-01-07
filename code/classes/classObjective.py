from classCable import Cable

class Objective():

    def __init__(self, cables, batteries):
        self.cables = cables
        self.batteries = batteries
        self._segmentCost = 9
        self._batteryCost = 5000
    
    def totalCost(self):
        cableSum = 0
        for cable in self.cables:
            cableSum += cable.calcLength()

        batterySum = len(self.batteries)

        total = cableSum * self._segmentCost + batterySum * self._batteryCost
        
        return total

