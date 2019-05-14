# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, room):
        self.room = room

    def __repr__(self):
        return self.room
