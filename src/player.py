# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, startRoom):
        self.currentRoom = startRoom
        self.inventory = []
        self.gold = 99

    def add_item(self, item):
        self.inventory.append(item)