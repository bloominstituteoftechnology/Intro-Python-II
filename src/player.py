# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.room = current_room
    def __repr__(self):
        return (f'name = {self.name}, room = {self.room}.')