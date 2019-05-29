# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, at_room):
        self.at_room = at_room

    def relocate (self, new_room):
        self.at_room = new_room

