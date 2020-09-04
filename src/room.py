# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, room_name, room_description, item):
        self.room_name = room_name
        self.room_description = room_description
        self.item = [item]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"Room: {self.room_name}, Description: {self.room_description}"

    def remove_item(self, item):
        del self.item[item]

    def add_item(self, item):
        self.item.append(item)