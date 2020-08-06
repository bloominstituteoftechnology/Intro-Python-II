# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room: Room, light_source_on: bool = False):
        self.name = name
        self.current_room = current_room
        self.light_source_on = light_source_on

    def __str__(self):
        return f'{self.name}, your adventure continues.\n \nLocation: {self.current_room.name}.\n \nWhat will you do?'