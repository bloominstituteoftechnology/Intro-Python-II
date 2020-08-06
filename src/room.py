# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []

    def get_direction(self, direction):
        """This function points the player to the inputted direction """
        if direction in ["n", "N"]:
            return self.n_to
        elif direction in ["s", "S"]:
            return self.s_to
        elif direction in ["w", "W"]:
            return self.w_to
        elif direction in ["e", "E"]:
            return self.e_to
        else:
            return None
