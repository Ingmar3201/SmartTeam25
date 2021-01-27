import time
import datetime

from classShare import Share

class SecondAlgorithm:
    '''
    Generates multiple solutions with the second algorithm and saves the best solution
    Utilizes in order: classGrid, classInitialSolution, classDensity and classShare
    '''

    def __init__(self, districts, gridAmount):
        startTime = time.time()
        prevMinute = 0.0

        theBestGrids = []
        nonFeasible = 0

        for district in districts:
            print("_______________________")
            print("Second Algorithm, District:", district)
            print("_______________________")

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
                    grid = Share(int(district))
                    grid.runShare()
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
            grid.makePlot(f"theBest_{now}", "Second Algorithm")
            grid.output(f"theBest_{now}", "costs-shared")

        print("________________________________________")
        print("Amount of non-feasible solutions:", nonFeasible)
        print("________________________________________")
        print("DONE!")