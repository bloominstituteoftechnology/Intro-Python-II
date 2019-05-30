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
        self.items = []

    
    # add items to a room
    def add_item(self, item):
        self.items.append(item)

    # remove items from a room
    def remove_item(self, item):
        self.items.remove(item)
        