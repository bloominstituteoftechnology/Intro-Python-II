# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, desc, satchel, location):
        self.name = name
        self.desc = name
        self.satchel = satchel
        self.location = location


    def __repr__(self):
        return '{self.__class__.__name__}({self.name}{self.satchel} {self.location})'.format(self=self)