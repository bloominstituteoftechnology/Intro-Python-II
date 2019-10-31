from color import Color

class Player:
    def __init__(self, name, loc, holding=[]):
        self.name = name
        self.loc = loc
        self.holding = holding

    def myItems(self):
        items = [i.name for i in self.holding]
        itemString = ', '.join(items)
        if len(items) > 0:
            itemString = f'You are holding {Color.RED}{items}{Color.END}'
        return itemString

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'
