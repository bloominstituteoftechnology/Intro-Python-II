# Implement a class to hold item information. This should have name and
# description attributes.


class Item:
    def __init__(self, name, short, long, full, light=False):
        self.name = name
        self.short = short
        self.long = long
        self.full = full
        self.light = light
