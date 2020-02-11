# Game declaration
from enum import Enum
from player import Player

class Direction(Enum):
    UP = "▲"
    RIGHT = "▶"
    DOWN = "▼"
    LEFT = "◀"

class Game:
    badChars = ["|", "-", "*"]

    def __init__(self):
        self.player = Player()
        self.map = [[]]
        with open ("map.txt", "r") as mapTxt:
            self.map = [self.split(line.rstrip()) for line in mapTxt]
            self.updatePlayer()


    def updatePlayer(self, direction = Direction.UP):
        self.map = self.map[self.player.y][:self.player.x] + [direction.value] + self.map[self.player.y][self.player.x + 1:]
        self.updateMap()

    def updateMap(self):
        print(self.player)
        for arr in self.map:
            print(self.convert(arr))

    def playerCanMove(self, direction):
        if direction == Direction.UP:
            if self.checkForChar(self.map[self.player.y - 1][self.player.x]):
                return False
            else:
                return True
        elif direction == Direction.DOWN:
            if self.checkForChar(self.map[self.player.y + 1][self.player.x]):
                return False
            else:
                return True
        elif direction == Direction.LEFT:
            if self.checkForChar(self.map[self.player.y][self.player.x - 1]):
                return False
            else:
                return True
        elif direction == Direction.RIGHT:
            if self.checkForChar(self.map[self.player.y][self.player.x + 1]):
                return False
            else:
                return True
        return False

    def moveUp(self):
        if self.playerCanMove(Direction.UP):
            self.player.moveUp()
            self.updatePlayer(Direction.UP)

    def moveDown(self):
        if self.playerCanMove(Direction.DOWN):
            self.player.moveDown()
            self.updatePlayer(Direction.DOWN)

    def moveLeft(self):
        if self.playerCanMove(Direction.LEFT):
            self.player.moveLeft()
            self.updatePlayer(Direction.LEFT)

    def moveRight(self):
        if self.playerCanMove(Direction.RIGHT):
            self.player.moveRight()
            self.updatePlayer(Direction.RIGHT)

    def split(self, str):
        return [char for char in str]  
    
    def convert(self, arr):
        string = ""
        for char in arr:
            string += char

        return string

    def checkForChar(self, char):
        for val in self.badChars:
            if val == char:
                return True
        return False