# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player(object):

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return str(self.current_room)
