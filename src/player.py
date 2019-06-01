# Write a class to hold player information, e.g. what room they are in
# currently.
# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name,room,items=[]):
        self.name = name
        self.room = room
        self.items = items
        self.score = 0


    def __str__(self):
        return self.items