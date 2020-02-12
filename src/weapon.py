from item import Item


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage
        