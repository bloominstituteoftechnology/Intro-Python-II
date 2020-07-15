# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player(Room):
    def __init__(self):
        super().__init__(room, description)

    def __str__(self):
        if self.room == 'outside':
            return f'You are {self.room}. {self.description}'
        else:
            return f'You are in the {self.room}. {self.description}'

    def __repr__(self):
        return f'room: "{self.room}" description: "{self.description}"'