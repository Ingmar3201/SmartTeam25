import csv
import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

from classHouse import House

def readHouse(houseData):
    """
    Reads data from csv file and creates house class per line
    All objects from class house are stored in a list
    """

    houses = []

    with open(houseData, 'r') as file:
        reader = csv.reader(file)
        next(file, None)

        for row in reader:
            house = House(row[0], row[1], row[2])
            houses.append(house)

    return houses