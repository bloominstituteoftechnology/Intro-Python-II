# Write a class to hold player information, e.g. what room they are in
# currently.
# note that room and player has items 
class Player:

    inventory = list()

    from room import Room
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def pick_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)