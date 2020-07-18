# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{self.name} is at {self.current_room.name}"

    def show_item(self):
        print(f'{self.name} has {len(self.inventory)} items:')
        for item in self.inventory:
            print(item.name)

    def get_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
