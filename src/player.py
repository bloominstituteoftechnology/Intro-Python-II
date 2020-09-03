# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        print(f"{self.name} is currently in {self.current_room}.")

    def change_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')

    def look(self):
        print(f"{self.name}, you find yourself in {self.current_room.name}. \n{self.current_room.description}")