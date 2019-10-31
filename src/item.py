from textwrap import wrap
from color import Color
from gameObj import GameObj

class Item(GameObj):
    def __init__(self, name, desc, useRooms={}):
        super().__init__(name, desc)
        self.useRooms = useRooms

    def useItem(self, room):
        if room not in self.useRooms:
            return f'You used the {self.name}, {Color.RED}nothing happened{Color.END}'
        else: 
            return self.useRooms[room]

    def __str__(self):
        return f'{Color.RED}{self.name}{Color.END}\n{Color.PURPLE}{self.desc}{Color.END}'
