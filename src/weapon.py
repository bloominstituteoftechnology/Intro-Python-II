from item import Item
#child of item
class Weapon(Item):
    def __init__(self, name, description, price, weight, style)
        super().__init__(name, description, price)
        self.weight = weight
        self.type = style
        