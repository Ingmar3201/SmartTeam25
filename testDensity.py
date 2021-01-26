import os, sys
import random
import time
import copy
import matplotlib.pyplot as plt
import datetime

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classGrid import Grid
from classInitialSolution import InitialSolution
#from classRandomSwap import RandomSwap
from classShare import Share
from classDensity import Density





for district in range(1,4):
    
    print(f"DISTRICT: {district}")
    print("_________________________________________")
    #grid = Share(int(district))
    #grid.runShare()
    grid = Density(int(district))
    grid.runDensity()
    print("_________________________________________")



"""
DISTRICT: 1
36547
_________________________________________
DISTRICT: 2
35890
_________________________________________
DISTRICT: 3
35467
"""