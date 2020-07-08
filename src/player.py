# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    """
    The Player class, keeps track of which room the player is in

    Attributes:
        current_room (Room): the room this player is currently in
    """

    def __init__(self, starting_room):
        """ Initializes a Player object, takes the room they start in """
        self.current_room = starting_room
    
    def move_to(self, new_room):
        """ Moves the player to a new room """
        self.current_room = new_room
