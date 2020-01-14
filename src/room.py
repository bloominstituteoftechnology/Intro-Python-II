# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    n_to = None
    s_to = None
    e_to = None
    w_to = None

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def roomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        else:
            return self.e_to