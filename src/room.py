# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return(f'{self.name} {self.description}\n\n \
        Items at current location: {self.items}\n \
        Direction options: [{self.getDirectionOptions()}]')

    def goNextRoom(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None

    def getDirectionOptions(self):
        dirOptions = []
        if self.n_to is not None:
            dirOptions.append('n')
        if self.s_to is not None:
            dirOptions.append('s')
        if self.e_to is not None:
            dirOptions.append('e')
        if self.w_to is not None:
            dirOptions.append('w')
        return ','.join(dirOptions)
    




    