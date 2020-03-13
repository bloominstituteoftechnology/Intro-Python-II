# Implement a class to hold room information. This should have title and
# description attributes.
from player import Player

class Room:
    """
    room class
    """
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
    def __str__(self):
        return f' {self.name}\n\n{self.description}'

    def room_inventory(self):
        if self.items is None:
            print('no items here')
        else:
            for item in self.items:
                print(f'there is a {item.name} ')
