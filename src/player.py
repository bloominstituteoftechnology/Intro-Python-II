# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(object):
    def __init__(self, name, room, items = []):
        self.name = name
        self.room = room
        self.items = items


