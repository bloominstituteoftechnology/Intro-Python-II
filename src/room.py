# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description

    def __str__(self):
        return f'You are {self.room}. {self.description}..\n'