class Item(object):
    """A game item."""
    def __init__(self, name, description, weight=0):
        self.name = name
        self.description = description
        self.is_light = False
        self.weight = weight


class Container(Item):
    """An Item that holds Items."""
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        self.locked = False
        self.key = None
        self.items = []


class Weapon(Item):
    """An attack Item."""
    def __init__(self, name, description, weight, attack):
        super().__init__(name, description, weight)
        self.attack = attack


class Shield(Item):
    """A shielding Item."""
    def __init__(self, name, description, weight, shield):
        super().__init__(name, description, weight)
        self.shield = shield
