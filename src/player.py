# Write a class to hold player information, e.g. what room they are in
# currently.
# note that room and player has items 
class Player:

    inventory = list()

    from room import Room
    def __init__(self, name, currentRoom: Room, items=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items