# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_up_item(self, item):
        self.current_room.items.remove(item)
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
        self.current_room.items.append(item)

    def __str__(self):
        return f"Name: {self.name}, current room: {self.current_room.items}, player inventory: {self.inventory}"