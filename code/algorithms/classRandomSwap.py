import os, sys
import random
import time
import matplotlib.pyplot as plt
import copy

from classInitialSolution import InitialSolution

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))


class RandomSwap(InitialSolution):
    '''
    Optimizes initial solution. Keeps swapping two randomly selected houses for certain time. Saves cheapest solution. 

    '''

    def runRandomSwap(self, runtime):
        '''
        Controls flow of random swap algorithm
        '''
        # get a initial solution (from classgrid)
        self.runInitialSolution()
        
        # set limiting parameters
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

        # make swaps during selected runtime
        while time.time() < endTime:
            
            # print time
            currentMinute = round((endTime - time.time())/60,1)
            if currentMinute != prevMinute:
                prevMinute = currentMinute

            # make one swap 
            self.randomSwap()
            reps += 1

        # reset cable configuration to best configuration
        self.replaceData(self.cablesBest)

        return True


    def randomSwap(self):
        '''
        Makes one swap between two houses 
        '''

        # select two random houses
        random.shuffle(self.houses)
        house0 = self.houses[0]
        house1 = self.houses[1]
        
        # if swap is possible within capacity of batteries make the swap
        if self.swap(house0, house1):
        
            # get paramaters of new configuration
            currentPrice = self.totalCost()
            cableSegmentList = self.cableSegmentList()
            cableSegmentSet = set(cableSegmentList)
            currentRepeatCableCount = len(cableSegmentList) - len(cableSegmentSet)

            # save the new configuration if it is an improvement 
            if currentPrice < self.bestPrice:
                self.bestPrice = currentPrice
                self.cablesBest = self.clone()
            
            # if swap causes total cost to exceed limiting parameters: reset to initial configuration
            if currentPrice > self.limitPrice or currentRepeatCableCount < self.initialRepeatCableCount:
                self.replaceData(self.initialCables)
            
        return True
