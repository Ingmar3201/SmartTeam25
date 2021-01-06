class House:
    
    def __init__(self, x, y, output):

        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
    
    def test(self):
        print(self.x, self.y, self.output)