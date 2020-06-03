# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from direction import Direction

class Player:
    def __init__(self, name: str, current_room: Room):
        self.name = name
        self.current_room = current_room

    def move(self, direction: Direction):

        room_to = None

        if direction == Direction.NORTH:
            room_to = self.current_room.n_to
        elif direction == Direction.SOUTH:
            room_to = self.current_room.s_to
        elif direction == Direction.EAST:
            room_to = self.current_room.e_to
        elif direction == Direction.WEST:
            room_to = self.current_room.w_to

        if room_to is not None:
            self.current_room = room_to
        else:
            print("There is no room to move to in that direction!\n")