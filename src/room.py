# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=[], n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = [Item(p) for p in items]
    def __str__(self):
        return f"<Room name: {self.name}, decription: {self.description}>\n"

    def get_items(self):
        print(f'{self.name} room has items as follows...')
        for item in self.items:
            print(f'{item.name}')
        print('\n')
            