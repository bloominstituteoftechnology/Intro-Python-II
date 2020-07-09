# Write a class to hold player information, e.g. what room they are in
# currently.

from item import LightSource

class Player():
    """
    The Player class, keeps track of which room the player is in

    Attributes:
        current_room (Room): the room this player is currently in
        items (list): a list of Items the player is holding
    """

    def __init__(self, starting_room):
        """ Initializes a Player object, takes the room they start in """
        self.current_room = starting_room
        self.items = []
    
    def move_to(self, new_room):
        """ Moves the player to a new room """
        self.current_room = new_room
    
    def drop_item(self, item_name):
        """ Drops an item from inventory """
        # Find the item with that name
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                # Remove the item from player's inventory and put it in
                # the current room
                item = self.items.pop(i)
                item.on_drop()
                self.current_room.add_item(item)                
                return
        
        print(f"You don't have a {item_name} to drop!")
    
    def has_light(self):
        """ returns true if the player is holding a light """
        for item in self.items:
            if type(item) == LightSource:
                return True

        # else
        return False
    
    def has_item(self, item_name):
        """ returns true if the player has the given item """
        for item in self.items:
            if item.name == item_name:
                return True

        # else
        return False
