# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    """
    The Room class, handles the room name and description, and keeps track of
    what other rooms can be moved to from here.

    Attributes:
        name (str): the name of this room
        description (str): the description of this room
        n_to (Room): the room to the north
        s_to (Room): the room to the south
        e_to (Room): the room to the east
        w_to (Room): the room to the west
    """

    def __init__(self, name, description):
        """ Initializes a room, takes a name and description """
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
