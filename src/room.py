# class for room attributes
from collections import defaultdict

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.contents = defaultdict(int)
        self.exits = {}

    def __str__(self):
        return(f'{self.name}\n\n{self.description}\n\n' +
               '\n'.join([key.description for key in self.contents.keys()]) +
               '\n\nExits: ' + ' '.join(list(self.exits.keys())))
