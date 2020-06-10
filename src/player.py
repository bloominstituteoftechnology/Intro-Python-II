# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item

class Player:
    def __init__(self, name, current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def __str__(self):
        return f'Name: {self.name}, Current Room: {self.current_room}'
    
    def move_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            print(f'The current room is {self.current_room}')
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('No room there, try another direction')
