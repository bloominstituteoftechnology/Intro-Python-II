# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item 

class Room:
    def __init__(self, name: str, description: str, inventory: List[Item] = []):
        self.name = name
        self.description = description
        self.inventory = inventory
    def __str__(self):
        return f"{self.name}"

    def print_description(self):
        return f"{self.subtext}"