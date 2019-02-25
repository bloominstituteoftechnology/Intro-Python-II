# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    def __str__(self):
        return f'player name: {self.name} current room: {self.currentRoom}'
