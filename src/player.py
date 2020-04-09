# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player(Room):
    def __init__(self,name,room):
        self.name = name
        self.current_room = room
    def __str__(self):
        return f'{self.name} is located at: {self.current_room}'
