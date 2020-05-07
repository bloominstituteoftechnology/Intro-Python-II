# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description,items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def add_items(self, item):
        self.items.append(item)

    def __str__(self):
        return f"you are in the {self.name}, {self.description} "


outside = Room('outside', 'the caves forward the cliff is backward', ['sword', 'dagger', 'axe'])
sword = Item('sword', 'longsilver')

outside.add_items(sword)

print(outside.items)