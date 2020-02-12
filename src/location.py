class Location:
    def __init__(self, x, y):
        self.x = x * 2 - 1
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x * 2

    def setY(self, y):
        self.y = y

    def addY(self, y):
        self.y += y

    def addX(self, x):
        self.x += x * 2
