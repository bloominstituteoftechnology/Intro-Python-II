# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f"{self.name} is currently in the {self.current_room} and holds the following items: {self.inventory}. "

