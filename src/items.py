class Item():
    """Parent item class"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}, {}, {}\n".format(self.name, self.description, self.value)

    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    def getisValue(self):
        return self.value

    def setName(self, newName):
        self.name = newName 
    def setDescription(self, newDescription):
        self.description = newDescription
    def setValue(self, newValue):
        self.value = newValue

    # def on_pickup(self):
    #     return "You dropped {}".format(self.name)

    # def on_drop(self):
    #     return "You picked {}".format(self.name)


class Silver(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                        description="A round coin with the bust of a forgotten king engraved on its front.",
                        value=self.amt
                    )

    def getAmt(self):
        return self.amt
    def setAmt(self, newAmt):
        self.amt = newAmt

    def __str__(self):
        return "{}\n".format(self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage, damageType, weaponType, status):
        self.damage = damage
        self.damageType = damageType
        self.weaponType = weaponType
        self.status = status
        super().__init__(name, description, value)
 
    def getDamage(self):
        return self.damage
    def getdamageType(self):
        return self.damageType
    def getweaponType(self):
        return self.weaponType
    def getStatus(self):
        return self.status

    def setDamage(self, newDamage):
        self.damage = newDamage
    def setdamageType(self, newdamageType):
        self.damageType = newdamageType
    def setweaponType(self, newweaponType):
        self.weaponType = newweaponType
    def setStatus(self, newStatus):
        self.status = newStatus

    def __str__(self):
        return "{}, {}, {}, {}\n".format(self.damage,
                                        self.damageType,
                                        self.weaponType,
                                        self.status)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                        description="A rock suitable for bludgeoning.",
                        value=0,
                        damage=2,
                        damageType="Blunt",
                        weaponType="Melee",
                        status="Normal"
                    )


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                        description="A tempered blade attached to a hilt. A testament to violence",
                        value=10,
                        damage=10,
                        damageType="Blunt",
                        weaponType="Melee",
                        status="Normal"
                    )

class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Bow",
                        description="A piece of curved wood tied to a string. Requires a keen eye",
                        value=10,
                        damage=10,
                        damageType="Pierce",
                        weaponType="Ranged",
                        status="Normal"
                    )


class Torch(Weapon):
    def __init__(self):
        super().__init__(name="Torch",
                        description="A small kindle of hope.",
                        value=0,
                        damage=5,
                        damageType="Pierce",
                        weaponType="Ranged",
                        status="Fire"
                    )


if __name__ == "__main__":
    ##### Class Declaration ######
    Silver = Silver(0)
    Rock = Rock()
    Sword = Sword()
    Bow = Bow()
    Torch = Torch()