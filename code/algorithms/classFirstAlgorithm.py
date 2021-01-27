import time
import datetime

from classRandomSwap import RandomSwap

class FirstAlgorithm():
    '''
    Generates multiple solutions with the first algorithm and saves the best solution
    Utilizes in order: classGrid, classInitialSolution and classRandomSwap
    '''
    
    def __init__(self, districts, gridAmount, runtime):
        startTime = time.time()
        prevMinute = 0.0

        theBestGrids = []
        nonFeasible = 0

        for district in districts:
            print("________________________________________")
            print("First Algorithm, District:", district, )
            print("________________________________________")
            
            grids = []
            iterations = 0
            
            # always generate enough grids
            while len(grids) < gridAmount + 1:
                
                # print the runtime about every 10th of a minute
                currentMinute = round((time.time() - startTime)/60,1)
                if currentMinute != prevMinute:
                    prevMinute = currentMinute
                    print(f"Runtime: {prevMinute} minutes,", "Iteration:", iterations)
                
                # creates a grid/randomswap object and runs the algorithm
                try:
                    grid = RandomSwap(int(district))
                    grid.runRandomSwap(runtime)
                    grids.append(grid)

                # non feasable solutions are counted but not saved
                except TypeError:
                    nonFeasible += 1

                iterations += 1

            bestGrid = grids[0]
            bestCost = grids[0].totalCost()

            # lookup the best solution of all the grids
            for grid in grids:
                cost = grid.totalCost()
                if cost < bestCost:
                    bestCost = cost
                    bestGrid = grid
            
            # saves the best grid of this district
            theBestGrids.append(bestGrid)
        
        # make a plot and a json output file of the best solution found
        now = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        for grid in theBestGrids:
            grid.makePlot(f"theBest_{now}", "First Algorithm")
            grid.output(f"theBest_{now}", "costs-shared")


        print("________________________________________")
        print("DONE!")
        print("Amount of non-feasible solutions:", nonFeasible)
        print(f"Plots in /plots with date and time: {now}")
        print(f"Output json in /results with date and time: {now}")