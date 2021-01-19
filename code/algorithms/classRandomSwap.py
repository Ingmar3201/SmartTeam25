import os, sys
import random
import time
import matplotlib.pyplot as plt
import copy

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

#from classBattery import Battery
#from classHouse import House
#from classGrid import Grid
#from readBattery import readBattery
#from readHouse import readHouse
#from vis import plot
#from classCable import Cable
#from bubblesort import bubblesort
#from bubblesortBattery import bubblesortBattery
#from classObjective import Objective
from classInitialSolution import InitialSolution


class RandomSwap(InitialSolution):

    def runRandomSwap(self, runtime):
        self.runInitialSolution()
        print(f"initial cost: {self.totalCost()}")

        self.bestPrice = self.totalCost()
        self.limitPrice = self.bestPrice * 1.2
        self.batteriesBest, self.cablesBest = self.clone()

        endTime = time.time() + runtime
        prevMinute = 0.0
        reps = 0

        while time.time() < endTime:
            reps += 1

            currentMinute = round((endTime - time.time())/60,1)
            if currentMinute != prevMinute:
                prevMinute = currentMinute
                print(f"remaining minutes: {prevMinute}, repeats: {reps}")

            self.randomSwap()
        
        print(f"DONE! repeats: {reps}")
        #print(f"last price: {self.totalCost()}")

        self.replaceData(self.batteriesBest, self.cablesBest)

        batterySet = set()
        for house in self.houses:
            batterySet.add(self.cables[house].battery)
        
        batteriesFromCables = list(batterySet)

        print(f"best price: {self.totalCost()}")

        for i in range(5):
            print(self.batteries[i].remainingCapacity())
            print(batteriesFromCables[i].remainingCapacity())

        return True


    def randomSwap(self):

        random.shuffle(self.houses)
        house0 = self.houses[0]
        house1 = self.houses[1]
        self.swap(house0, house1)
        
        improvedPrice = self.totalCost()

        if improvedPrice < self.bestPrice:
            self.bestPrice = improvedPrice
            self.batteriesBest, self.cablesBest = self.clone()
            print(f"better price: {self.totalCost()}")
            self.output("bestOut")            

        if improvedPrice > self.limitPrice:
            self.batteries.clear()
            self.cables.clear()
            self.addBatteries()
            self.runInitialSolution()

        return True
     

# district 1: min objective: 53188
# district 2: min objective: 45268
# district 3: min objective: 42757