# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, location):
        self.location = location
        self.name = name
        self.inventory = []
    def add_item(self, item):
        item.on_take()
        self.inventory.append(item)

    def drop_item(self, stri):
        for a in self.inventory:
            if a.name == stri:
                self.inventory.remove(a)
                a.on_drop()
                return a 
