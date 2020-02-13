# Game declaration
import os
from enum import Enum
from entity import Player, Enemy
from direction import Direction, TermColors
from item import Weapon, WeaponType, PotionType

class Game:
    specialChar = ["|", "-", "*", "x", "@", "▲", "▶", "▼", "◀"]

    def __init__(self, enemies = [Enemy(10, 10, 1), Enemy(11, 10, 1)]):
        self.player = Player()
        self.enemies = enemies
        self.map = [[]]
        self.items = []
        with open("map.txt", "r") as mapTxt:
            for line in mapTxt.readlines():
                self.map.append(self.split(line.rstrip()))
            self.updatePlayer(self.player.getPreviousLocation())

    def updatePlayer(self, previousLocation, direction = Direction.UP, isTick = True):
        self.map[previousLocation[1]][previousLocation[0]] = " "
        self.map[self.player.getY()][self.player.getX()] = direction.value
        self.updateMap(isTick)

    def updateMap(self, isTick = True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(f"{TermColors.OKGREEN}{self.player}{TermColors.ENDC}")
        # 🛡
        if isTick:
            self.updateEntities()
            print("Tick")
        else:
            print("Not tick")
        for arr in self.map:
            print(self.convert(arr))

    def entityCanMove(self, direction, entity):
        x = entity.getX()
        y = entity.getY()
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
        previousLocation = self.player.getPreviousLocation()
        if self.entityCanMove(Direction.UP, self.player):
            self.player.moveUp()
            self.updatePlayer(previousLocation, Direction.UP)
        else:
            self.updatePlayer(previousLocation, Direction.UP, False)

    def moveDown(self):
        previousLocation = self.player.getPreviousLocation()
        if self.entityCanMove(Direction.DOWN, self.player):
            self.player.moveDown()
            self.updatePlayer(previousLocation, Direction.DOWN)
        else:
            self.updatePlayer(previousLocation, Direction.DOWN, False)

    def moveLeft(self):
        previousLocation = self.player.getPreviousLocation()
        if self.entityCanMove(Direction.LEFT, self.player):
            self.player.moveLeft()
            self.updatePlayer(previousLocation, Direction.LEFT)
        else:
            self.updatePlayer(previousLocation, Direction.LEFT, False)

    def moveRight(self):
        previousLocation = self.player.getPreviousLocation()
        if self.entityCanMove(Direction.RIGHT, self.player):
            self.player.moveRight()
            self.updatePlayer(previousLocation, Direction.RIGHT)
        else:
            self.updatePlayer(previousLocation, Direction.RIGHT, False)

    # def performAction():
        # if

    def updateEntities(self):
        for enemy in self.enemies:
            directionList = []
            for direction in Direction:
                if self.entityCanMove(direction, enemy):
                    directionList.append(direction)

            prevLoc = enemy.getPreviousLocation()
            enemy.move(self.player, self.map, directionList)
            self.map[prevLoc[1]][prevLoc[0]] = " "
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