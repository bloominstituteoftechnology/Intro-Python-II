# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from direction import Direction
from drop import Drop
from typing import List

class Player:
    def __init__(self, name: str, room: Room):
        self.name = name
        self.room = room
        self.drops: List[Drop] = []

    def move(self, direction: Direction):

        next_room: Room = None

        if direction == Direction.north:
            next_room = self.room.north
        elif direction == Direction.south:
            next_room = self.room.south
        elif direction == Direction.east:
            next_room = self.room.east
        elif direction == Direction.west:
            next_room = self.room.west

        if next_room is not None:
            self.room = next_room
        else:
            print('No Room')

    def allow(self, direction: Direction):
        if direction == Direction.north:
            return self.room.north is not None
        elif direction == Direction.south:
            return self.room.south is not None
        elif direction == Direction.east:
            return self.room.east is not None
        elif direction == Direction.west:
            return self.room.west is not None   

    def pick_up(self, drop: Drop):
        self.room.drops.remove(drop)
        self.drops.append(drop)
        drop.pick_up()

    def put_down(self, drop: Drop):
        self.drops.remove(drop)
        self.room.drops.append(drop)
        drop.put_down