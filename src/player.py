# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room

    def get_location(self):
        return self.room

    def set_location(self, room):
        self.room = room