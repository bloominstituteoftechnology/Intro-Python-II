from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = []

    def pickup_item(self, item):
        self.inventory.append(item)
    
    def try_move(self, direction):