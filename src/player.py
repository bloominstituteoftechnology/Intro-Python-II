# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''The player; holds current room'''
    def __init__(self, initial_room):
        self.current_room = initial_room

    def enter_room(self, room):
        self.current_room = room
