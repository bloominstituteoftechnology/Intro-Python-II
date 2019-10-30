# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name):
        self.name = name
        return

    def __repr__(self):
        return f'Player({repr(self.name)})'

    def __str__(self):
        return f'Player: {self.name}'

    def current_room(self, room):
        self.room = room
    