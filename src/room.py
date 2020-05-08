# Implement a class to hold room information. This should have name and
# description attributes.

from typing import List
from item import Item 
from inventory_holder import Inventory_Holder

class Room:
    def __init__(self, name: str, description: str, inventory: List[Item] = []):
        self.name = name
        self.description = description
        self.inventory = inventory

    def show_inventory(self):
        print("This is what's in our inventory: \n")
        # this is how to check for empty list in Python

        for item in self.inventory:
            print(item)

    def item_transfer(self, item: Item, other):
        self.inventory.remove(item)
        print(f"{item.name} has been removed from {self.name}'s inventory")
        other.inventory.append(item)
        print(f"{item.name} has been added to {other.name}'s inventory")

    # spawn item in inventory
    def item_spawn(self, item: Item):
        self.inventory.append(item)
      #  print(f"{item.name} has been spawned and added to {self.name}'s inventory")
        print(item.name, "has been spawned to", self.name, "and added to their inventory")
    
    def print_description(self):
        return f"{self.description}"