# Implement a class to hold room information. This should have name and
# description attributes.


class Room():

    def __init__(self, name, desc):
        # Initialize name and desc during creation.
        self.name = name
        self.desc = desc

        # Place holder for mapping adjacent rooms.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
