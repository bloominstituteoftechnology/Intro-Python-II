# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
class Player:
    def _init__(self, name, inRoom):
        self.name = name
        self.inRoom = inRoom