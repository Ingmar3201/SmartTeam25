import csv
from classBattery import CBattery
from classHouse import House

"""
house objects by Freek
"""
houses = []

with open("../data/district_1/district-1_houses.csv", 'r') as file:
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

"""
battery objects by Ingmar
"""
batteries = []

with open("../data/district_1/district-1_batteries.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        battery = CBattery(row[0], row[1])
        battery.coordinates()
        batteries.append(battery)

"""
for bat in batteries:
    print(bat.x, bat.y)
    print(bat.capacity)
    """