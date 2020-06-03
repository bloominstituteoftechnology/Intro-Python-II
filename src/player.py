
'''
Creates a player object that contains a name, and what the current room location is.
'''


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        if self.current_room.description is not None:
            description = self.current_room.description
        return 'You currently in' + self.current_room + '.\n' + description

    def __repr__(self):
        return 'Player({self.name}, {self.current_room})'.format(self=self)
