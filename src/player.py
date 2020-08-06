# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    def __init__(self, name, current_room, items =[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def next_move(self, direction):
        '''This function controls the players movement'''
        new_room = self.current_room.get_direction(direction)
        if new_room is not None:
            self.current_room = new_room
            print(self.current_room)
        else:
            print("Uh oh, That is not a valid direction! Try again!")
