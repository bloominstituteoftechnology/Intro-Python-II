# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
    
    def move(self, dir):
        getattr(self.current_room, dir)
        if hasattr(self.current_room, dir):
            self.current_room = getattr(self.current_room, dir)
