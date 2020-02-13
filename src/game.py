# Game declaration
import os
from enum import Enum
from entity import Player, Enemy
from location import Direction, TermColors
from item import Weapon, WeaponType, PotionType

class Game:
    def __init__(self, mapFile, enemies = [Enemy(10, 10, 1), Enemy(11, 10, 1)]):
        self.player = Player()
        self.enemies = enemies
        self.map = [[]]
        self.items = []
        with open(mapFile, "r") as mapTxt:
            for line in mapTxt.readlines():
                self.map.append(self.split(line.rstrip()))
            self.updatePlayer(self.player.getPreviousLocation())

    def updatePlayer(self, previousLocation, direction = Direction.UP, isTick = True):
        self.map[previousLocation[1]][previousLocation[0]] = " "
        self.map[self.player.getY()][self.player.getX()] = direction.value
        self.updateMap(isTick)

    def updateMap(self, isTick = True):
        os.system('cls' if os.name == 'nt' else 'clear')
        # 🛡
        if isTick:
            self.updateEntities()
            print("Tick")
        else:
            print("Not tick")
        printMap = f"\n{TermColors.OKGREEN}{self.player}{TermColors.ENDC}\n"
        for arr in self.map:
            printMap += self.convert(arr)
        print(printMap)

    def move(self, direction):
        previousLocation = self.player.getPreviousLocation()
        if self.player.entityCanMove(direction, self.map):
            if direction == Direction.UP:
                self.player.moveUp()
            elif direction == Direction.LEFT:
                self.player.moveLeft()
            elif direction == Direction.RIGHT:
                self.player.moveRight()
            elif direction == Direction.DOWN:
                self.player.moveDown()
            self.updatePlayer(previousLocation, direction)
        else:
            self.updatePlayer(previousLocation, direction, False)

    # def performAction():
        # if

    def updateEntities(self):
        for enemy in self.enemies:
            enemy.updateEntity(self.map, self.player)


    def split(self, str):
        return [char for char in str]
    
    def convert(self, arr):
        string = ""
        for char in arr:
            string += char
        return string