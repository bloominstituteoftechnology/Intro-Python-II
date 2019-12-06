# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_name(self):
        return self.name

    def get_location(self):
        return self.current_room

    def set_location(self, new_room):
        self.current_room = new_room
