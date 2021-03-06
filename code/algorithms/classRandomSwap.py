import random
import time

from classInitialSolution import InitialSolution


class RandomSwap(InitialSolution):
    '''
    Optimizes initial solution. Keeps swapping two randomly selected houses for certain time. Saves best solution. 

    '''

    def runRandomSwap(self, runtime):
        '''
        Controls flow of random swap algorithm
        '''
        # get a initial solution (from class initialsolution)
        self.runInitialSolution()
        
        # set limiting parameter
        self.bestPrice = self.totalCost()
        self.limitPrice = self.bestPrice * 1.001

        # saves the intial cable configuration and defaults best cables (method of class grid)
        self.initialCables = self.clone()
        self.cablesBest = self.initialCables

        # make list of all cable points
        cableSegmentList = self.cableSegmentList()
        cableSegmentSet = set(cableSegmentList)

        # calculate all points that repeat in the intial solution
        self.initialRepeatCableCount = len(cableSegmentList) - len(cableSegmentSet)

        endTime = time.time() + runtime

        # make swaps during selected runtime
        while time.time() < endTime:

            # make one swap 
            self.randomSwap()


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
        
        # if swap is possible within capacity of batteries make the swap (method in class grid)
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
