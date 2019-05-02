from room import Room
from player import Player


class Item(object):
    def __init__(self, item):
        self.name = item[0]
        self.description = item[1]

    def __repr__(self):
        return f'{self.name}, {self.description}'

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
