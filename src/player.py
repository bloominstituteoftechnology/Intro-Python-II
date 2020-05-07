# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"name: {self.name}, current room: {self.current_room}, inventory: {self.inventory}"

    def pickup_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)

    def drop_item(self, item):
        self.inventory.remove(item)
        self.current_room.items.append(item)