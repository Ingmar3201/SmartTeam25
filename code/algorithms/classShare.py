import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
#sys.path.append(os.path.join(directory, "code", "algorithms"))
#sys.path.append(os.path.join(directory, "code", "visualisation"))

from classInitialSolution import InitialSolution


# per batterij alle kabels af gaan
    # voor een kabel: # zoek vanaf huis tot batterij 
        # punt voor punt, naar bijliggende kabels in de y richting
            # wordt er iets gevonden
                # check of: 
                    # het een huis is, 
                    # of het bij dezelfde batterij hoort
                    # en of de huis niet al is gebruikt
                # neem alle kabel punten over
                # stop als de kabel in de y richting gaat

class Share(InitialSolution):
    
    def runShare(self):
        
        self.runInitialSolution()
        print(f"initial cost: {self.totalCost()}")

        self.getLocation()

        battery = self.batteries[0]
        houses = self.housesPerBattery(battery)
        house = houses[1]
        houseFound = False
        cable = self.cables[house]
        print(f"battery location {battery.x},{battery.y}")
        print(cable.x)
        print(cable.y)
        previousY = cable.y[0]
        for i in range(len(cable.x)):
            x = cable.x[i]
            y = cable.y[i]
            if previousY != y:
                break

            searchLocations = [f"{x},{y+1}" , f"{x},{y-1}"]
            for location in searchLocations:
                if location in self.houseLocations:
                    if self.houseLocations[location] in houses:
                        houseFound = self.houseLocations[location]
                        break
            
            if houseFound != False:
                break

        if houseFound != False:
            pass
            



            



    def getLocation(self):
        self.houseLocations = {}
        for house in self.houses:
            location = f"{house.x},{house.y}"
            self.houseLocations[location] = house
        
        return True




