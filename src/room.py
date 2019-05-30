# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
import textwrap


class Room():

    def __init__(self, name, desc):
        # Initialize name and desc during creation.
        self.name = name
        self.desc = desc

        # Place holder for mapping adjacent rooms.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        # Place holder for items
        self.items = []

    def __str__(self):
        output = f'{self.name}: '

        for text in textwrap.wrap(self.desc):
            output += "\n" + text

        return output

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, index):
        self.items.pop(index)
