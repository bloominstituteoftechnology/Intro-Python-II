# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room
    def __repr__(self):
        return f"Player is in {self.room}"