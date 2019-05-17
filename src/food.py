#child of item
from item import Item
#child of item
class Food(Item):
    def __init__(self, name, price, is_gluten_free, energy)
        super().__init__(name, price)
        self.is_gluten_free = is_gluten_free
        self.energy = energy
       