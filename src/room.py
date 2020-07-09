# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
    def __repr__(self):
        return (f'Room Name = {self.name}, Room Description = {self.description}.')