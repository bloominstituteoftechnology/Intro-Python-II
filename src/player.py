# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

#change
class Player:
    # * Properties
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    # * Methods
    def set_current_room(self, new_room):
        self.current_room = new_room

    def get_item(self, item):
        self.inventory.append(item)

    def __repr__(self):
        return f"Player is in {self.current_room}"
