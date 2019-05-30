# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def __str__(self):
        return f'You are currently located {self.current_room}'