import csv
from classHouse.py import House

with open("../data/district_1/district-1_houses.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        House(row[0], row[1], row[2])

