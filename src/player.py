# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item
from typing import List


class Player:
    def __init__(self, name: str, current_room: Room, items: List[Item] = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move_to(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            return getattr(self.current_room, f'{direction}_to')
        return None
