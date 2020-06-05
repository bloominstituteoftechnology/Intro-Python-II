# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f' {self.name}, {self.current_room}'

    def cardinal_dir(self, cardinal_direction):
        
        location = self.current_room.mapping(cardinal_direction)

        if location != None:
            self.current_room = location
        
        else:
            print('Error: no room here, movement not allowed...')
