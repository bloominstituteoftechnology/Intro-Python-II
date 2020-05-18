# Write a class to hold player information, e.g. what room they are in
# currently.
"""
Ready Player 1

Attributes:
    -name
    -current_room

Methods:
    -add items to player inventory - picked up from room
    -remove item from player inventory - player drops into current room

"""
from item import Item

class Player(Item):
    def __init__(self, name, room, item = []):
        super().__init__(item)
        self.name = name
        self.room = room
        
    ### add item function, append item to the item list
    def add_item(self, item):
        self.item.append(item)
    
   ### remove item function, remove item from list     
    def drop_item(self, item):
        self.item.remove(item)
        
    def __str__(self):
       return f"Player Name: {self.name} \nPlayers {self.room} \nItems in Bag of Holding: {self.item}"
