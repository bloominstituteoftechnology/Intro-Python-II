# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    """
    A simple player class
    Params - 
        name - a string containing the players name
    Attributes - Defaults to None, user must define after instantiating
        current_room - a reference to the current room the player is in
    """

    def __init__(self, name):
        self.name = name
        self.current_room = None