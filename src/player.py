# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, loc, holding=[]):
        self.name = name
        self.loc = loc
        self.holding = holding

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'
