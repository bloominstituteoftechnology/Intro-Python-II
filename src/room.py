# Implement a class to hold room information. This should have name and
# description attributes.
from collections import defaultdict


class Room:
    def __init__(self,
                 name,
                 description,
                 dark_desc='It\'s pitch black. You can\'t see a thing!',
                 lit=False):
        self.name = name
        self.description = description
        self.dark_desc = dark_desc
        self.lit = lit
        self.contents = defaultdict(int)
        self.exits = {}

    def __str__(self, player_light=False):
        light_in_room = False
        for item in self.contents.keys():
            light_in_room = light_in_room or item.light
        if not (self.lit or light_in_room or player_light):
            room_string = f'Darkness\n\n{self.dark_desc}'
        else:
            room_string = f'{self.name}\n\n{self.description}'
            if len(self.contents) != 0:
                room_string += ('\n\n' + \
                                '\n'.join([key.long for key in \
                                       self.contents.keys()]))
            room_string += ('\n\nVisible exits: ' + \
                            ' '.join(list(self.exits.keys())))
        return room_string

    def has_light(self):
        light_in_room = False
        for item in self.contents.keys():
            light_in_room = light_in_room or item.light
        return self.lit or light_in_room
