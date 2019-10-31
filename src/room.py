# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):
    """A room in the game.

    :var name: str - name of the room
    :var description: str - description of room

    """

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.items_ = {}
        self.characters = {}
        self.light = True
        self.to_n = None
        self.to_s = None
        self.to_w = None
        self.to_e = None
