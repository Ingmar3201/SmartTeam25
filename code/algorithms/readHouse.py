"""
house objects by Freek
"""

import csv
import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from classHouse import House

def readhouse(houseData):

    houses = []

    with open(houseData, 'r') as file:
        reader = csv.reader(file)
        next(file, None)
        for row in reader:

            houses.append(House(row[0], row[1], row[2]))

    return houses