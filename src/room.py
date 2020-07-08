# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item


class Room:
    def __init__(self, name: str, description: str, items: List[Item] = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, item: Item):
        self.items.append(item)
