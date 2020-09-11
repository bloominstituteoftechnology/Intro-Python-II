# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.name}: \n{self.description}"

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to {self.name}")