from enum import Enum

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

class Direction(Enum):
    UP = "▲"
    RIGHT = "▶"
    DOWN = "▼"
    LEFT = "◀"

class TermColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"