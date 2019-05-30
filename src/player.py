# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item


class Player():

    def __init__(self, name):
        # Initialize name during creation
        self.name = name

        # Place holder for current room information
        self.current_room = None

        # Place holder for items
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, index):
        self.items.pop(index)

    def set_current_room(self, room):
        self.current_room = room

    def get_current_room(self):
        return self.current_room
