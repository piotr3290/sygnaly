class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x.__str__() + " " + self.y.__str__()
