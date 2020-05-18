# Implement a class to hold room information. This should have name and
# description attributes.

""" 
The Room of Doom. Beware the Mindflayer...

Attributes:
-name
-description
-directions
    -n_to
    -s_to
    -e_to
    -w_to
    
Methods:
    -add items to room, because player dropped item
    -remove items from room, because player picked item up

"""
from item import Item

class Room(Item):
    def __init__(self, name, description, item = []):
        super().__init__(item)
        self.name = name
        self.description = description
        
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
   
   ### add item function, append item to the item list
    def add_item(self, item):
        self.item.append(item)
    
   ### remove item function, remove item from list     
    def drop_item(self, item):
        self.item.remove(item)
        
    
    def __str__(self):
        return f"Location: {self.name} \nDescription: {self.description} \nItems in room: {self.item} "