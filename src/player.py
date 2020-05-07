# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name: str, location: Room):
        self.name = name 
        self.location = location

    def __str__(self):
        return str(self.__dict__)