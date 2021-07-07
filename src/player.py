# Write a class to hold player information, e.g. what room they are in
# currently.

# Attributes
# name
# current_room

class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items
    def __str__(self):
        return f"Player: {self.name}"
    def __repr__(self):
        return f"Player({repr(self.name, self.room)})"
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)