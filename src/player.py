# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, items, awake=True):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.awake = awake