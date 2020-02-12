# Game declaration
import os
from enum import Enum
from entity import Player, Enemy
from item import Weapon, WeaponType, PotionType

class TermColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class Direction(Enum):
    UP = "▲"
    RIGHT = "▶"
    DOWN = "▼"
    LEFT = "◀"

class Game:
    specialChar = ["|", "-", "*", "x", "@"]

    def __init__(self, enemies = [Enemy(True, False, 10, 10, 1), Enemy(True, False, 11, 10, 1)], Items = []):
        self.player = Player()
        self.enemies = enemies
        self.previousLocation = (self.player.getX(), self.player.getY())
        self.map = [[]]
        with open("map.txt", "r") as mapTxt:
            for line in mapTxt.readlines():
                self.map.append(self.split(line.rstrip()))
            self.updatePlayer()

    def updatePlayer(self, direction = Direction.UP, isTick = True):
        self.map[self.previousLocation[1]][self.previousLocation[0]] = " "
        self.map[self.player.getY()][self.player.getX()] = direction.value
        self.previousLocation = (self.player.getX(), self.player.getY())
        self.updateMap(isTick)

    def updateMap(self, isTick = True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(f"{TermColors.OKGREEN}{self.player}{TermColors.ENDC}")
        # 🛡
        if isTick:
            self.updateEntities()
        for arr in self.map:
            print(self.convert(arr))

    def entityCanMove(self, direction):
        x = self.player.getX()
        y = self.player.getY()
        if direction == Direction.UP:
            if self.checkForChar(self.map[y-1][x]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.DOWN:
            if self.checkForChar(self.map[y+1][x]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.LEFT:
            if self.checkForChar(self.map[y][x-1]) or self.checkForChar(self.map[y][x-2]):
                self.updateMap(False)
                return False
            else:
                return True
        elif direction == Direction.RIGHT:
            if self.checkForChar(self.map[y][x+1]) or self.checkForChar(self.map[y][x + 2]):
                self.updateMap(False)
                return False
            else:
                return True
        return False

    def moveUp(self):
        if self.entityCanMove(Direction.UP):
            self.player.moveUp()
            self.updatePlayer(Direction.UP)
        else:
            self.updatePlayer(Direction.UP, False)

    def moveDown(self):
        if self.entityCanMove(Direction.DOWN):
            self.player.moveDown()
            self.updatePlayer(Direction.DOWN)
        else:
            self.updatePlayer(Direction.DOWN, False)

    def moveLeft(self):
        if self.entityCanMove(Direction.LEFT):
            self.player.moveLeft()
            self.updatePlayer(Direction.LEFT)
        else:
            self.updatePlayer(Direction.LEFT, False)

    def moveRight(self):
        if self.entityCanMove(Direction.RIGHT):
            self.player.moveRight()
            self.updatePlayer(Direction.RIGHT)
        else:
            self.updatePlayer(Direction.RIGHT, False)

    # def performAction():
        # if

    def updateEntities(self):
        for enemy in self.enemies:
            self.map[enemy.getY()][enemy.getX()] = "x"



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