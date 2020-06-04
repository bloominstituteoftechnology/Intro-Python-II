# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.enlightened = False

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'