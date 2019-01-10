# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, inventory = []):
        self.name = name
        self.inventory = inventory
        self.room = room
    def __repr__(self):
        return f"{self.name} is in {self.room}"