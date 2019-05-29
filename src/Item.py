# This is the file for the Item class and other Item subclasses. Each Item will include at least a name and description.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up the {self.name}.")

    def on_drop(self):
        print(f"You have dropped the {self.name}.")

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
