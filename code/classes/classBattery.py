class Battery():
    def __init__(self, position, capacity):
        self._position = position
        self.capacity = float(capacity)

    def extractCoordinates(self):
        self.x = 0
        self.y = 0
        temp = ""

        for letter in self._position:
            if letter == ",":
                self.x = int(temp)
                temp = ""
            else:
                temp += letter
        self.y = int(temp)
