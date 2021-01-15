import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))

from classGrid import Grid

grid = Grid(1)

print(f"can add houses = {grid.addHouses()}")
print(f"amount of houses in grid = {len(grid.houses)}")
print("____________________________________")
print(f"can add batteries = {grid.addBatteries()}")
print(f"amount of batteries in grid = {len(grid.batteries)}")
print("____________________________________")

house = grid.houses[58]
battery = grid.batteries[0]

print(f"can make connection = {grid.makeConnection(house, battery)}")
print(f"cable connection: {grid.cables[house]}: {grid.cables[house].battery} - {grid.cables[house].house}")

cable = grid.cables[house]
print(cable)
print(f"house location: {cable.house.x}, {cable.house.y}")
print(f"battery location: {cable.battery.x}, {cable.battery.y}")
print(cable.x)
print(cable.y)
print(len(cable.x) == len(cable.y))
print(len(cable.x))
print(cable.calcLength())

"""
print(f"can make connection = {grid.makeConnection(house, battery)}")
print(f"cable connection: {grid.cables[house]}: {grid.cables[house].battery} - {grid.cables[house].house}")
print(f"battery total output: {battery.totalOutput}")
print(f"total cables: {len(grid.cables)}")
print("____________________________________")

print(f"can remove connection = {grid.removeConnection(house)}")
#print(f"cable connection: {grid.cables[house]}: {grid.cables[house].battery} - {grid.cables[house].house}")
print(f"can remove connection = {grid.removeConnection(house)}")
print(f"battery total output: {battery.totalOutput}")
print(f"total cables: {len(grid.cables)}")

print("____________________________________")
print(f"can check connection before add = {grid.hasConnection(house)}")
grid.makeConnection(house, battery)
print(f"can check connection after add = {grid.hasConnection(house)}")
print(f"total cables: {len(grid.cables)}")
"""

