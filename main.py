import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from classSecondAlgorithm import SecondAlgorithm
from classFirstAlgorithm import FirstAlgorithm

districtsToRun = [1]
amountOfSolutionsToGenerate = 1
secondsToRunPerSolution = 1

print("_________________________________")
print("|        First Algorithm        |")
print("|_______________________________|")
first = FirstAlgorithm(districtsToRun, amountOfSolutionsToGenerate, secondsToRunPerSolution)

print("_________________________________")
print("|        Second Algorithm       |")
print("|_______________________________|")
second = SecondAlgorithm(districtsToRun, amountOfSolutionsToGenerate)