from item import Item
#child of item
class Attire(Item):
    def __init__(self, name, price, material, color)
        super().__init__(name, price)
        self.material = material
        self.color = color 
