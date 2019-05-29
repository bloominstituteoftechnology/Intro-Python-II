# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name):
        self.room = room
        self.name = name
        self.items = []
