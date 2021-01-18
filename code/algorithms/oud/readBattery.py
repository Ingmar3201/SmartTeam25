import os, sys
import csv

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code", "classes"))

from classBattery import Battery

def readBattery(batteryData):
    """
    Reads data from csv file and creates battery class per line
    All objects from class battery are stored in a list
    """

    batteries = []

    id = 0
    with open(batteryData, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        
        for row in reader:
            battery = Battery(row[0], row[1])
            battery.extractCoordinates()
            battery.id = id
            batteries.append(battery)
            id += 1
            
    return batteries