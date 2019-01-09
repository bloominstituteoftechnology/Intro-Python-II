class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__()
            self.name = name
            self.description = description




class Weapon(Item):
    def __init__(self, variety, damagePoints):
        super().__init__(name, description)
            self.variety = variety
            self.damagePoints = damagePoints

class Sword(Weapon)
    def __init__(self, ):
        super().__init__(variety, damagePoints)