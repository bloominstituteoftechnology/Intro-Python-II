# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

direction_names = {
    'n': 'North',
    'e': 'East',
    'w': 'West',
    's': 'South'
    }


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
