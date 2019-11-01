# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.items = items

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        
    def __str__(self):
        return str(self.name)
        return str(self.description)

    def __repr__(self):
        return f'Room: {repr(self.name)}'

    