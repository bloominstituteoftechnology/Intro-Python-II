class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'a {self.name}'

class LightSource(Item):

    def __init__(self, name, description, isLit: bool = True, durability: int = 100):
        super().__init__(name, description)
        self.isLit = isLit
        self.durability = durability

    def decrementDurability(self):
        self.durability -= 1

        if self.durability == 0:
            self.isLit = False