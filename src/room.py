# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description,items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def on_drop(self, item):
        self.items.append(item)
        print(f'{item} has been dropped into room ')

    def on_take(self, item):
        self.items.remove(item)
        print(f'{item} has been taken from room ')

    def __str__(self):
        return f"you are in the {self.name}, {self.description} "

