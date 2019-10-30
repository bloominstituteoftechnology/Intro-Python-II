# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name):
        self.name = name
        self.player = []

    def __repr__(self):
        return f'Room({repr(self.name)})'

    def __str__(self):
        return f'Room: {self.name}'

    def room(self):

        return 