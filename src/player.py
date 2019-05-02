# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    def __init__(self, name: str, room: Room):
        self.name = name
        self.room = room

    def __str__(self):
        return str(self.__dict__)

    def getRoom(self):
        return str(self.room)