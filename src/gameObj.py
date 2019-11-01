from textwrap import wrap
from color import Color

class GameObj:
    def __init__(self, name, desc, holding=[], isDark=False):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.holding = holding
        self.isDark = isDark
        self.seen = False

    def showItems(self):
        if self.isDark == True:
            return None
        items = [i.name for i in self.holding]
        itemString = ', '.join(items)
        if len(items) > 0:
            itemString = f'{Color.RED}{items}{Color.END}'
            return itemString
        else: return None

    def __str__(self):
        return f'++ {self.name}\n\f{self.desc} ++'