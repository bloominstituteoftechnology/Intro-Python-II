from random import random
from enum import Enum
from location import Location

class Item:
    def __init__(self, name = "Item", value = 0, x = -1, y = -1):
        self.name = name
        self.value = value
        self.damage = 1
        self.location = Location(x, y)
    
    def getX(self):
        return self.location.getX()

    def getY(self):
        return self.location.getY()

    def getLocation(self):
        return (self.getX(), self.getY())

    def setLocation(self, x, y):
        self.location = Location(x, y)

    def removeFromGround(self):
        self.location = Location(-1, -1)

class Effect(Enum):
    HEALING = 0

class PotionType(Enum):
    HEALING = ("Healing", Effect.HEALING)

class WeaponType(Enum):
            # Name, BaseDmg, val
    FISTS = ("Fists",  1,    -1 )
    SWORD = ("Sword",  4,     10)
    AXE =   ("Axe",    3,     7 )
    CLUB =  ("Club",   3,     4 )

class WeaponEffect(Enum):
                # Name,      dmg, val
    NO_EFFECT = ("null",      0,  0 )
    DULL =      ("Dull",     -1, -3 )
    SHARP =     ("Sharpened", 1,  2 )
    BROKEN =    ("Broken",   -2, -5 )
    GODLY =     ("Godly",     3,  20)
    EVIL =      ("Evil",      1,  5 )
    HOLY =      ("Holy",      1,  5 )

class Weapon(Item):
    def __init__(self, weapon = WeaponType.FISTS, x = -1, y = -1, effect = None):
        super(Weapon, self).__init__(weapon.value[0], weapon.value[2], x, y)
        self.damage = weapon.value[1]
        self.effect = effect
        self.totalDamage = self.damage
        if self.name != "Fists" and effect == None:
            self.getRandomAttr()

    def getRandomAttr(self):
        attrIndex = int(random() * (len(WeaponEffect)))
        self.effect = list(WeaponEffect)[attrIndex]
        
    def getName(self):
        return f"{self.effect.value[0]} {self.name}"
    
    def getDamage(self):
        return self.totalDamage

    def __str__(self):
        if self.effect == None:
            return f"{self.name}"
        return f"{self.getName()}"