# class for player information and attributes
from collections import defaultdict

class Adventurer:
    def __init__(self, room):
        self.room = room
        self.inventory = defaultdict(int)