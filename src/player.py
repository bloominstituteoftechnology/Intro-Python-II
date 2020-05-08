# Write a class to hold player information, e.g. what room they are in
# currently.

from typing import List, Generic
from item import Item
from inventory_holder import Inventory_Holder

class Player(Inventory_Holder):
    def __init__(self, name, location, inventory: List[Item]=[]):
        self.name = name
        self.location = location
        self.inventory = inventory 

    def show_inventory(self):
        print("This is what's in our inventory: \n")
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

    def move_to(self, direction, current_loc):
        # try to move in the specified direction 
        attribute = direction + '_to'

        # if we can move in specified direction from our current location 
        if hasattr(current_loc, attribute):
            # get the room in the specified 
            return getattr(current_loc, attribute)
        
        # if we can't go that way 
        print("You can't go that way\n")

        return current_loc
