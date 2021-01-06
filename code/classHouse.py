class House:
    
    def __init__(self, x, y, output):

        self.x = x
        self.y = y
        self.output = output
    
    def test(self):
        print(self.x, self.y, self.output)