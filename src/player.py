# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player(Room):
    def __init__(self):
        super().__init__(room, description)

    def __repr__(self):
        return f'room: "{self.room}" description: "{self.description}"'