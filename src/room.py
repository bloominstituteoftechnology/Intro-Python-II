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
        room_string = f'{self.name}\n\n{self.description}'
        if len(self.contents) != 0:
            room_string += ('\n\n' + \
                            '\n'.join([key.long for key in \
                                       self.contents.keys()]))
        room_string += ('\n\nVisible exits: ' + \
                        ' '.join(list(self.exits.keys())))
        return room_string
