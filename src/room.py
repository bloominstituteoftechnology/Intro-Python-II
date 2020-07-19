# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, description, items=[]):
        self.room = room
        self.description = description
        self.items = items

    def __str__(self):
        return f'\nYou are {self.room}. \n{self.description}..\n'