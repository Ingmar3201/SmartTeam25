import time
import datetime

from classRandomSwap import RandomSwap

class FirstAlgorithm():
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
            while len(grids) < gridAmount:
                currentMinute = round((time.time() - startTime)/60,1)
                if currentMinute != prevMinute:
                    prevMinute = currentMinute
                    print(f"Runtime: {prevMinute} minutes,", "Iteration:", iterations)
                try:
                    grid = RandomSwap(int(district))
                    grid.runRandomSwap(runtime)
                    grids.append(grid)
                except TypeError:
                    print("type error")
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
            grid.makePlot(f"theBest_{now}", "First Algorithm")
            grid.output(f"theBest_{now}", "costs-shared")

        print("________________________________________")
        print("Amount of non-feasible solutions:", nonFeasible)
        print("________________________________________")
        print("DONE!")