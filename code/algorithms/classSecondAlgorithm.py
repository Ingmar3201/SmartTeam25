import time
import datetime

from classShare import Share

class SecondAlgorithm:
    def __init__(self, districts, repeats):
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
            while len(grids) < repeats:
                currentMinute = round((time.time() - startTime)/60,1)
                if currentMinute != prevMinute:
                    prevMinute = currentMinute
                    print(f"Runtime: {prevMinute} minutes,", "Iteration:", iterations)
                try:
                    grid = Share(int(district))
                    grid.runShare()
                    grids.append(grid)
                except TypeError:
                    nonFeasible += 1

                iterations += 1

            bestGrid = grids[0]
            bestCost = grids[0].totalCost()

            for grid in grids:
                cost = grid.totalCost()
                if cost < bestCost:
                    bestCost = cost
                    bestGrid = grid
            
            theBestGrids.append(bestGrid)

        for grid in theBestGrids:
            now = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            grid.makePlot(f"theBest_{now}", "Second Algorithm")
            grid.output(f"theBest_{now}", "costs-shared")


        print("Amount of non-feasible solutions:", nonFeasible)