# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item
from typing import List

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

        self.items: List[Item] = []

        
