# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        return f"Player({self.name}) at {repr(self.current_room)}"

    def __str__(self):
        return f"{self.name}"

