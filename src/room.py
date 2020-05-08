# Implement a class to hold room information. This should have name and
# description attributes.
from collections import defaultdict


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.contents = defaultdict(int)
        self.exits = {}

    def __str__(self):
        return(f'{self.name}\n\n{self.description}\n\n' +
               '\n'.join([key.long for key in self.contents.keys()]) +
               '\n\nVisible exits: ' + ' '.join(list(self.exits.keys())))
