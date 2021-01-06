import csv
from classHouse import House

houses = []
with open("../data/district_1/district-1_houses.csv", 'r') as file:
    reader = csv.reader(file)
    next(file, None)
    for row in reader:
        print(row)
        houses.append(House(row[0], row[1], row[2]))

print("---")
for i in houses:
    i.test()