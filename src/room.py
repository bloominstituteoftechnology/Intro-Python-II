# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    name = ""
    description = ""

    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.e_to = "nope"
        self.w_to = "nope"
        self.n_to = "nope"
        self.s_to = "nope"
