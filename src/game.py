# Game declaration
from enum import Enum
from player import Player
import os

class Direction(Enum):
    UP = "▲"
    RIGHT = "▶"
    DOWN = "▼"
    LEFT = "◀"

class Game:
    specialChar = ["|", "-", "*"]

    def __init__(self):
        self.player = Player()
        self.previousLocation = (self.player.x, self.player.y)
        self.map = [[]]
        with open ("map.txt", "r") as mapTxt:
            for line in mapTxt.readlines():
                self.map.append(self.split(line.rstrip()))
            self.updatePlayer()

    def updatePlayer(self, direction = Direction.UP):
        self.map[self.previousLocation[1]][self.previousLocation[0]] = " "
        self.map[self.player.y][self.player.x] = direction.value
        self.previousLocation = (self.player.x, self.player.y)
        self.updateMap()

    def updateMap(self, isTick = True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(self.player)
        for arr in self.map:
            print(self.convert(arr))

        if isTick:
            print("update tick") # TODO: Create enemies and update their location every tick

    def playerCanMove(self, direction):
        if direction == Direction.UP:
            if self.checkForChar(self.map[self.player.y - 1][self.player.x]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.DOWN:
            if self.checkForChar(self.map[self.player.y + 1][self.player.x]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.LEFT:
            if self.checkForChar(self.map[self.player.y][self.player.x - 1]) or self.checkForChar(self.map[self.player.y][self.player.x - 2]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.RIGHT:
            if self.checkForChar(self.map[self.player.y][self.player.x + 1]) or self.checkForChar(self.map[self.player.y][self.player.x + 2]):
                self.updateMap(False)
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
        for val in self.specialChar:
            if val == char:
                return True
        return False