# Implement a class to hold room information. This should have name and
# description attributes.

# title and description

# create your constructor

# have parameters with the n,s, stuff

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):

        return f'room: {self.name}\ndescription: {self.description}\nexits: {self.getRoomExitString()}\nitems: {self.items}'


    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)
