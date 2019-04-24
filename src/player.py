# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        new_room = self.current_room.adjacent_room_for(direction)
        self.current_room = new_room

    def look(self):
        self.current_room.list_visible_items()