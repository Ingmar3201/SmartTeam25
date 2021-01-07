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
cables = []

testBat = batteries[0]
testHouse = houses[0]
cableTest = Cable(testHouse, testBat)

#print(testBat.addHouse(testHouse))

cables.append(cableTest)

print(f"x coordinate of house = {cables[0].house.x}")
print(f"y coordinate of house = {cables[0].house.y}")
print(f"x coordinate of battery = {cables[0].battery.x}")
print(f"y coordinate of battery = {cables[0].battery.y}")