# Write a class to hold player information, e.g. what room they are in
# currently.
from inventory_holder import Inventory_Holder

class Player(Inventory_Holder):
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory 

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
