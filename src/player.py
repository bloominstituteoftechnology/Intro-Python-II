# Write a class to hold player information, e.g. what room they are in
# currently.
from lib import NameStorage

class Player(NameStorage):
    def __init__(self, name, current_room, storage = []):
	    super().__init__(name, storage = storage)
	    self.current_room = current_room

    def move_player(self, new_room):
        self.current_room = new_room
