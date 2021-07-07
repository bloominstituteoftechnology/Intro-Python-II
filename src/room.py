"""
BeWilder - text adventure game :: Room definition

A class to hold room information - name and description attributes.
"""

from __future__ import annotations
import textwrap

from adv_utils import justify_center, table_maker
from item import Item


class Room:
    def __init__(
        self,
        name: str,
        description: str,
        n_to: Room = None,
        s_to: Room = None,
        e_to: Room = None,
        w_to: Room = None,
    ):
        """Constructor for the Room base class.
        
        :param name        (str) : Short name of the room.
        :param description (str) : Description of room.
        :param n_to        (str) : Name of room to the north.
        :param s_to        (str) : Name of room to the south.
        :param e_to        (str) : Name of room to the east.
        :param w_to        (str) : Name of room to the west.
        """
        # Set name of this room instance
        self.name = name

        # Set up neighboring rooms
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

        # Set up the description to print nicely
        self.description = description

        # List to hold items in room
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.name.lower()] = item

    def __str__(self):
        print_string = f"{self.name}\n{self.description}\n\n"
        # Create dictionary of item names and descriptions
        item_dict = {item.name: item.description for key, item in self.items.items()}
        # Use that dictionary to generate a table
        print_string += table_maker(item_dict, "Available items")
        return print_string

    def __repr__(self):
        return f"{self.name}"
