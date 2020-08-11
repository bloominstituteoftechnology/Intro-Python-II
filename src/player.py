# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
    def __init__(self, name):
        super().__init__(name, description)
        self.name = name
        
    def __str__(self):
        return f"{self.name}: {self.room}"