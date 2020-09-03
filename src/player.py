# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player: 
    def __init__(self,name, location):
        self.name = name
        self.location = location
        self.items = []

    def add_item_to_player(self, name, description):
        item = Item(name, description)
        self.items.append(item)

    def __str__(self):
        return f"{self.name}: {self.location}"