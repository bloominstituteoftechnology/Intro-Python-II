import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"You have picked up {self.name}")
    def on_drop(self):
        print(f"You have dropped {self.name}")

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
    def attack(self):
        print(random.randrange(1, self.damage))

class Healing(Item):
    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing
