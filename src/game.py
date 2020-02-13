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
        self.prevLoc = (self.player.getX(), self.player.getY())
        self.map = [[]]
        self.items = []
        with open(mapFile, "r") as mapTxt:
            for line in mapTxt.readlines():
                self.map.append(self.split(line.rstrip()))
            self.updatePlayer()

    def updatePlayer(self, direction = Direction.UP, isTick = True):
        self.map[self.prevLoc[1]][self.prevLoc[0]] = " "
        self.map[self.player.getY()][self.player.getX()] = direction.value
        self.player.setDirection(direction)
        self.prevLoc = (self.player.getX(), self.player.getY())
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
        if self.player.entityCanMove(direction, self.map):
            if direction == Direction.UP:
                self.player.moveUp()
            elif direction == Direction.LEFT:
                self.player.moveLeft()
            elif direction == Direction.RIGHT:
                self.player.moveRight()
            elif direction == Direction.DOWN:
                self.player.moveDown()
            self.updatePlayer(direction)
        else:
            self.updatePlayer(direction, False)

    def performAction(self):
        direction = self.player.getDirection()
        location = (self.player.getX(), self.player.getY())
        if direction == Direction.UP:
            location = (location[0], location[1] - 1)
        elif direction == Direction.DOWN:
            location = (location[0], location[1] + 1)
        elif direction == Direction.LEFT:
            location = (location[0] - 2, location[1])
        elif direction == Direction.RIGHT:
            location = (location[0] + 2, location[1])
        for item in self.items:
            if item == None:
                continue
            else:
                itemLocation = item.getLocation()
                if itemLocation[0] == location[0]//2 + 1 and itemLocation[1] == location[1]:
                    self.player.addItemToInv(item)
                    self.updatePlayer(self.player.getDirection(), True)
        for index, enemy in enumerate(self.enemies):
            enemyLocation = enemy.getCurrentLocation()
            print(f"Enemy health: {enemy.getHealth()}, enemy location: {enemyLocation}, location in front of player: ({location[0]//2 + 1}, {location[1]})")
            if enemyLocation[0] == location[0]//2 + 1 and enemyLocation[1] == location[1]:
                enemy.removeHealth(self.player.getDamage())
                print(enemy.checkIfDead())
                if enemy.checkIfDead():
                    print("Dead")
                    del(self.enemies[index])
                    self.items.append(enemy.dropItem())
                self.updatePlayer(self.player.getDirection(), True)

    def switchWeapon(self, index):
        self.player.setSelectedWeapon(index)

    def updateEntities(self):
        for enemy in self.enemies:
            enemy.updateEntity(self.map, self.player)

    def updateItems(self):
        for item in self.items:
            self.map[item.getY()][item.getX()] = "+"

    def split(self, str):
        return [char for char in str]
    
    def convert(self, arr):
        string = ""
        for char in arr:
            string += char
        return string