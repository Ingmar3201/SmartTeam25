"""
battery objects by Ingmar
"""

import os, sys
import csv

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from classBattery import Battery

def readBattery(batteryData):
    batteries = []

    with open(batteryData, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            battery = Battery(row[0], row[1])
            battery.extract_coordinates()
            batteries.append(battery)


    #for bat in batteries:
    #    print(bat.x, bat.y)
    #    print(bat.capacity)
