# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):

        return f'name: {self.name}, room: {self.current_room}'

    name = str
    current_room = str

