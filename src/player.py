# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.currentRoom = currentRoom
        self.name = name
        self.inventory = []
    def __str__(self):
        return f'{self.name} is in {self.currentRoom}.'