import os, sys
import csv

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from classBattery import Battery
from classHouse import House
from readBattery import readBattery

"""
house objects by Freek
"""
houses = []

with open("data/district_1/district-1_houses.csv", 'r') as file:
    reader = csv.reader(file)
    next(file, None)
    for row in reader:
        #print(row)
        houses.append(House(row[0], row[1], row[2]))
"""
print("---")
for i in houses:
    i.test()
"""

readBattery("data/district_1/district-1_batteries.csv")