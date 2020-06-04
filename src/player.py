# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room)
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if self.currect_room.connections [direction] is not None:
            self.currect_room = self.current_room.connections[direction]
        else:
            print("You cannot move in that direction.")