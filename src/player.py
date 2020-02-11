# Player and Weapon class declaration

from item import Weapon, WeaponType

class Player:
    def __init__(self, x = 3, y = 34, health = 10, level = 1, xp = 0):
        self.x = x
        self.y = y
        self.health = health
        self.level = level
        self.inventory = []
        self.xp = xp
        self.levelxp = []
        for val in range(1, 11):
            self.levelxp.append(2 ** val)
        self.weapon = Weapon()
        self.updateDamage()

    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

    def moveLeft(self):
        self.x -= 2

    def moveRight(self):
        self.x += 2

    def takeHealth(self, health):
        self.health -= int(health)
        if health <= 0:
            self.die()

    def giveHealth(self, health):
        self.health += int(health)
        if health > 10:
            health = 10

    def giveXp(self, xp):
        self.xp += xp
        if xp >= self.levelxp[0]:
            self.xp -= self.levelxp[0]
            self.level += 1
            self.levelxp.remove(self.levelxp[0])

    def getHealth(self):
        return "♥" * self.health

    def getXp(self):
        return self.xp

    def getDamage(self):
        return int(self.damage * self.weapon.damage)

    def updateDamage(self):
        self.damage = int(self.level * self.weapon.damage)

    def die(self):
        self = Player(level = self.level)

    def __str__(self):
        return f"Health: {self.getHealth()}, {self.weapon}, Damage: {self.getDamage()} Level: {self.level}, XP: {self.xp}/{self.levelxp[0]}"
