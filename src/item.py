from textwrap import wrap
from color import Color

class Item:
    def __init__(self, name, desc, useRooms={}):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.useRooms = useRooms

    def useItem(self, room):
        if room not in self.useRooms:
            return f'You used the {self.name}, {Color.RED}nothing happened{Color.END}'
        else: 
            return self.useRooms[room]

    def __str__(self):
        return f'{Color.RED}{self.name}{Color.END}\n{Color.PURPLE}{self.desc}{Color.END}'
