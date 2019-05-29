"""Creates an item class and subclasses with name, description, other attributes."""

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Food(Item):
    def __init__(self, name, description, energy_value):
        super().__init__(name, description)
        self.energy_value = energy_value