# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
        items = [None]

    def __str__(self):
        return f"Hello {self.name}. Your current location is: {self.cur_room}"