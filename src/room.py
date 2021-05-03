# Implement a class to hold room information. This should have name and
# description attributes.

from typing import Dict, Optional
from item import Item


class Room:
    def __init__(self, name: str,
                 description: Optional[str] = None,
                 items: Optional[Dict[Item, int]] = None
                 ):
        self.name = name
        self.description = description if description is not None else "No description given!"
        self.items = items if items is not None else {}
        self.branches = {
            "north": None,
            "east": None,
            "south": None,
            "west": None,
        }

    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"

    def __str__(self):
        n = self.branches["north"]
        e = self.branches["east"]
        s = self.branches["south"]
        w = self.branches["west"]

        items_desc = ", ".join([f"{item}" for item in self.items])

        return f"""
----------------------
Room: {self.name}
- Description: {self.description}
- Items: [{items_desc}]
- Branches: 
    north={n.name if n is not None else "None"}, 
    east={e.name if e is not None else "None"}, 
    south={s.name if s is not None else "None"}
    west={w.name if w is not None else "None"}
        """

    def add_item(self, item: Item):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1

    def remove_item(self, item: Item):
        if item not in self.items:
            return
        self.items[item] -= 1
        if self.items[item] == 0:
            del self.items[item]

    def create_branch_map(self,
                          north: Optional["Room"],
                          east: Optional["Room"],
                          south: Optional["Room"],
                          west: Optional["Room"],
                          ):
        self.branches["north"] = north
        self.branches["east"] = east
        self.branches["south"] = south
        self.branches["west"] = west