# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_up_item(self):
        removedItem = self.current_room.items.pop()
        addedItem = self.inventory.append(removedItem)
        return addedItem

    def __str__(self):
        return f"Name: {self.name}, current room: {self.current_room.items}, player inventory: {self.inventory}"