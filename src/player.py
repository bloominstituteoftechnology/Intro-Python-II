# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, currentLoc):
        self.name = name
        self.currentLoc = currentLoc
        self.items = []


    def __repr__(self):
        return self.name

    def addItems(self, *items):
        self.items.append(*items)