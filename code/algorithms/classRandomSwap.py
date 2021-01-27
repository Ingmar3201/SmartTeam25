'''
Algorithm to improve optimize solution. Keeps swapping two randomly selected houses for certain time. Saves cheapest solution. 

'''


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
        '''
        Control flow of random swap algorithm
        '''
        # set initial parameters
        self.runInitialSolution()
        #print(f"initial cost: {self.totalCost()}")
        self.bestPrice = self.totalCost()
        self.limitPrice = self.bestPrice * 1.001
        self.initialCables = self.clone()
        self.cablesBest = self.initialCables
        
        cableSegmentList = self.cableSegmentList()
        cableSegmentSet = set(cableSegmentList)
        self.initialRepeatCableCount = len(cableSegmentList) - len(cableSegmentSet)

        # set runtime
        endTime = time.time() + runtime
        prevMinute = 0.0
        reps = 0

        # run swap algorithm for selected runtime
        while time.time() < endTime:
            
            # print time
            currentMinute = round((endTime - time.time())/60,1)
            if currentMinute != prevMinute:
                prevMinute = currentMinute
                #print(f"remaining minutes: {prevMinute}, repeats: {reps}")

            # make swap 
            self.randomSwap()
            reps += 1

        #print(f"DONE! repeats: {reps}")
        #print(f"last price: {self.totalCost()}")

        self.replaceData(self.cablesBest)
        #print(f"best price: {self.totalCost()}")
        return True


    def randomSwap(self):
        '''
        Makes swap between two houses 
        '''

        # select two random houses
        random.shuffle(self.houses)
        house0 = self.houses[0]
        house1 = self.houses[1]
        
        # If swap is possible within capacity of batteries make swap
        if self.swap(house0, house1):
        
            # save new configuration
            currentPrice = self.totalCost()
            cableSegmentList = self.cableSegmentList()
            cableSegmentSet = set(cableSegmentList)
            currentRepeatCableCount = len(cableSegmentList) - len(cableSegmentSet)

            # check for improvement in configuration
            if currentPrice < self.bestPrice:
                self.bestPrice = currentPrice
                self.cablesBest = self.clone()
                #print(f"better price: {self.totalCost()}")
                #self.output("bestOut")

            #print(currentRepeatCableCount)

            # if swap exceeds limiting parameters reset to initial configuration
            if currentPrice > self.limitPrice or currentRepeatCableCount < self.initialRepeatCableCount:
                self.replaceData(self.initialCables)
                #self.batteries.clear()
                #self.cables.clear()
                #self.addBatteries()
                #self.runInitialSolution()

        return True
     
'''
district 1: min objective: 53188
district 2: min objective: 45268
district 3: min objective: 42757
'''