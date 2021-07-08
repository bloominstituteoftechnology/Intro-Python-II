# Implement a class to hold room information. This should have name and
# description attributes.
class Room: 
    def __init__(self, name, desc, item):
        self.name = name
        self.desc = desc
        self.item = item

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}{self.desc})'.format(self=self)