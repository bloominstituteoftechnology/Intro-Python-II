from textwrap import wrap
from color import Color

class Room:
    def __init__(self, name, desc, holding=[]):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.holding = holding
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def printItems(self):
        items = [i.name for i in self.holding]
        itemString = ', '.join(items)
        if len(items) > 0:
            itemString = f'You can see {Color.RED}{items}{Color.END}'
        return itemString

    def __str__(self):
        itemString = self.printItems()
        return f"{Color.PURPLE}>> {self.name} <<{Color.END}\n\f{self.desc}\n"+f"\f{itemString}"