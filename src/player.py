# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player(Room):
    def __init__(self, room, description, name):
        super().__init__(room, description)
        self.name = name

    def __str__(self):
        if self.room == 'outside':
            return f'{self.name}! You are {self.room}. {self.description}'
        elif self.room == 'treasure':
            return f'{self.name}! You have found the {self.room}. {self.description}'
        else:
            return f'{self.name}! You are in the {self.room}. {self.description}'

    def __repr__(self):
        return f'{self.room} {self.description}'