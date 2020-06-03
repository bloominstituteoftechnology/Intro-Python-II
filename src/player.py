# Write a class to hold player information, e.g. what room they are in
# currently.

class Adventurer:
    def __init__(self, room):
        self.room = room
        # self.inventory = defaultdict(int) for day 2 mvp