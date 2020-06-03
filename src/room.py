# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        # Name and description
        self.name = name
        self.desc = desc
        # connections to other room objects
        self.n_to = None    # North
        self.w_to = None    # West
        self.s_to = None    # South
        self.e_to = None    # East
