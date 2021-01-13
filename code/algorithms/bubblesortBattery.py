import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))

def bubblesortBattery(battery, house):
    unsorted = battery
    sorted = []

    for i in range(len(battery)):
        minBattery = battery[0]
        for j in range(len(unsorted)):
            if battery[j].calcLength(house) < minBattery.calcLength(house):
                minBattery = battery[j]
        sorted.append(minBattery)
        unsorted.remove(minBattery)

    return sorted

