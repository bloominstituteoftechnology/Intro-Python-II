# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):
    """A room in the game."""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
        self.characters = {}
        self.to_n = None
        self.to_s = None
        self.to_w = None
        self.to_e = None
