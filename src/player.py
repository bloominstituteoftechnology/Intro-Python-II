# Write a class to hold player information, e.g. what room they are in
# currently.

# Put the Player class in player.py.
# Players should have a name and current_room attributes

class Player:

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory