directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))

from classCable import Cable

def objective(cables, batteries):
    """
    A function to calculate the objective function
    The objective function is the total price of the network
    """
    segmentCost = 9
    batteryCost = 5000
    
    cableSum = 0
    for cable in cables:
        cableSum += cable.calcLength()

    batterySum = len(batteries)

    total = cableSum * segmentCost + batterySum * batteryCost
    
    return total

