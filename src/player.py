# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    inventory = list()

    from room import Room
    def __init__(self, name, currentRoom: Room):
        self.currentRoom = currentRoom