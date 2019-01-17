# Write a class to hold player information, e.g. what room they are in
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def __repr__(self):
        return f"{self.name} is in {self.current_room}"
# currently.
