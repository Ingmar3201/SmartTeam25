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
from classRandomSwap import RandomSwap
from classShare import Share

runtime = 60 * 0.05

now = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
name = f"terminalOutput/terminal_{now}.txt"

#with open(name, 'w') as f:
#    sys.stdout = f

for district in range(2,3):
    
    print(f"DISTRICT: {district}")
    print("_________________________________________")
    #grid = 0
    grid = Share(int(district))
    grid.runShare()
    #grid.makePlot()

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