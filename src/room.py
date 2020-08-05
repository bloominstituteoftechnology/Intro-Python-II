# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None, items: [Item] = [], isLit: bool = False):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
        self.isLit = isLit

    def __str__ (self):
        if self.isLit:
            if len(self.items) == 0:
                return f'\nRoom: {self.name}\nDescription: {self.description}\n'
            else:
                return f'\nRoom: {self.name}\nDescription: {self.description}\nYou see {self.items} in the area.'

        else:
            return f'\nThe dark is all consuming.\nYou cannot see anything.'