from textwrap import wrap
from color import Color

class Room:
    def __init__(self, name, desc, holding=[]):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.holding = holding
        self.seen = False
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.u_to = None
        self.d_to = None

    def roomItems(self):
        items = [i.name for i in self.holding]
        itemString = ', '.join(items)
        if len(items) > 0:
            itemString = f'You can see {Color.RED}{items}{Color.END}'
        return itemString

    def __str__(self):
        return f'{self.desc}\n'