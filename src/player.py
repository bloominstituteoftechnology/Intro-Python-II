# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, storage=[]):
        self.name = name
        self.current_room = starting_room
        self.storage = storage
    
    def storageString(self):
        return ', '.join([item.name for item in self.storage])