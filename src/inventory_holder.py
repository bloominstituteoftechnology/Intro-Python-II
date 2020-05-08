# this class be be defined as a generic class
# for doing type annotations


from typing import List, Generic
from item import Item

class Inventory_Holder:
    def __init__(self, name:str, inventory: List[Item] = []):
        self.name = name
        self.inventory = inventory

    def show_inventory(self):
        print("This is what's in the inventory: \n")
        for item in self.inventory:
            print(item)

    def item_transfer(self, item: Item, other):
        self.inventory.remove(item)
        print("{item.name} has been removed from {self.name}'s inventory")
        other.inventory.append(item)
        print("{item.name} has been added to {self.name}'s inventory")

    # spawn item in inventory
    def item_spawn(self, item: Item):
        self.inventory.append(item)
        print("{item.name} has been spawned and added to {self.name}'s inventory")