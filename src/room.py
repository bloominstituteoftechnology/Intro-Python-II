"""
BeWilder - text adventure game :: Room definition

A class to hold room information - name and description attributes.
"""

from __future__ import annotations
import textwrap

from utils import justify_center


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
        # self.display_width = 40
        # self.justified_name = justify_center(self.name, self.display_width, "-")

    def __str__(self):
        return f"{self.name}\n{self.description}"

    def __repr__(self):
        return f"{self.name}\n{self.description}"
