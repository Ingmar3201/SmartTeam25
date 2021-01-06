import csv

with open("../data/district_1/district-1_batteries.csv", 'r') as file:
    reader = csv.reader(file)
    next(file, None)
    for row in reader:
        position = row[0]

x = 0
y = 0
temp = ""

for letter in position:
    if letter != ",":
        temp += letter
        print(temp)
