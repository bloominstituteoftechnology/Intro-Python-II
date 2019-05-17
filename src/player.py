# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, inv = []):
        self.name = name
        self.room = room
        self.inv = inv

    def __str__(self):
        return f"Hello! I'm {self.name} and I'm holding {self.inv}."