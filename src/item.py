from random import random
from enum import Enum

class Item:
    def __init__(self, name = "Item", value = 0):
        self.name = name
        self.value = value

class Effect(Enum):
    HEALING = 0

class PotionType(Enum):
    HEALING = ("Healing", Effect.HEALING)

class WeaponType(Enum):
            # Name, BaseDmg, val
    FISTS = ("Fists",  1,    -1)
    SWORD = ("Sword",  4,     10)
    AXE =   ("Axe",    3,     7)
    CLUB =  ("Club",   3,     4)

class WeaponEffect(Enum):
             # Name,      dmg, val
    DULL =   ("Dull",     -1, -3 )
    SHARP =  ("Sharpened", 1,  2 )
    BROKEN = ("Broken",   -2, -5 )
    GODLY =  ("Godly",     3,  20)
    EVIL =   ("Evil",      1,  5 )
    HOLY =   ("Holy",      1,  5 )

class Weapon(Item):
    def __init__(self, weapon = WeaponType.FISTS):
        super(Weapon, self).__init__(weapon.value[0], weapon.value[2])
        self.damage = weapon.value[1]
        self.totalDamage = self.damage
        if self.name != "Fists":
            self.getRandomAttr()


    def getRandomAttr(self):
        attrs = {"Dull": -1, "Sharpened": 1, "Broken": -2, "Godly": 2, "Evil":  1, "Holy": 1}
        attrIndex = int(random() * (len(attrs)))
        super.name = f"{attrs[attrIndex]} {self.name}"
    
    def __str__(self):
        return f"Weapon: {self.name}"