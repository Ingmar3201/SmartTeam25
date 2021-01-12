import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))

def bubblesort(houses):
    unsorted = houses
    sorted = []

    for i in range(len(houses)):
        maxHouse = houses[0]
        for j in range(len(unsorted)):
            if houses[j].output > maxHouse.output:
                maxHouse = houses[j]
        sorted.append(maxHouse)
        unsorted.remove(maxHouse)

    return sorted

