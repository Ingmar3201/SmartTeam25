class Battery():
    '''
    Defines the components of a battery object
    '''

    def __init__(self, position, capacity, id):
        self._position = position
        self.capacity = float(capacity)
        self.totalOutput = 0.0
        self.id = id


    def extractCoordinates(self):
        '''
        The coordinates are given as a singular string
        This method stores them in separate variables
        '''
        self.x = -1
        self.y = -1
        temp = ""

        for letter in self._position:

            # everything before the comma belongs to the x-coordinate
            if letter == ",":
                self.x = int(temp)
                temp = ""
            else:
                temp += letter
                
        # the remaining characters belong to the y-coordinate
        self.y = int(temp)

        # validate the coordinates
        return self.x >= 0 and self.y >= 0


    def remainingCapacity(self):
        '''
        Return the capacity that can still be filled by output
        '''
        return self.capacity - self.totalOutput


    def calcLength(self, house):
        '''
        Calculates the length between this battery and a house with Manhattan distance
        '''
        length = abs(house.x - self.x) + abs(house.y - self.y)
        return length