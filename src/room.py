# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description

    def __str__(self):
        if self.room == 'outside':
            return f'You are {self.room}. {self.description}'
        else:
            return f'You are in the {self.room}. {self.description}'

    def __repr__(self):
        return f'room: "{self.room}" description: "{self.description}"'