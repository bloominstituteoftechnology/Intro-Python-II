# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def take(self, item):
        self.items.append(item)
        
    def drop(self, item):
        self.items.remove(item)

    def inventory(self):
        print(f" I'm in my bag {self.items}")