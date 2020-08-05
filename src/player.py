# Write a class to hold player information, e.g. what room they are in
# currently.
from src.room import Room

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []

    def move(self, direction):
        '''This function controls player movement'''
        new_room = self.current_room.get_direction(direction)
        if new_room is not None:
            self.current_room = new_room
            print(self.current_room)
        else:
            print("You cannot move in this direction.")
