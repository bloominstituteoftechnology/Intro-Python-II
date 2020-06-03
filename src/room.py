'''
Creates a room object that has a name and a description
'''


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'The room is called: {self.name}.\n{self.description}'.format(self=self)

    def __repr__(self):
        return 'Room({self.name}, {self.description})'.format(self=self)
