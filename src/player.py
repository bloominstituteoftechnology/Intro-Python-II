# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room, Items=[]):
        self.name = name
        self.current_room = current_room
        self.Items = Items

    def __str__(self):
        print(self.name, self.current_room, self.Items)

    def __repr__(self):
        return self