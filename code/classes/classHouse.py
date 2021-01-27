class House:
    """
    Defines the structure of a house object
    """
    def __init__(self, x, y, output, id):
        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
        self.id = id
