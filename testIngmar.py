import os, sys
import csv

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from classBattery import Battery
from classHouse import House
from classCable import Cable
from classObjective import Objective
from readBattery import readBattery
from readHouse import readHouse

houses = readHouse("data/district_1/district-1_houses.csv")
batteries = readBattery("data/district_1/district-1_batteries.csv")

cableTest = []
cableTest.append(Cable(houses[0], batteries[0]))

print(f"house x = {houses[0].x}, house y = {houses[0].y}, battery x = {batteries[0].x}, battery y = {batteries[0].y}")
print(cableTest[0].calcLength())

objTest = Objective(cableTest, batteries)
print(objTest.totalCost())