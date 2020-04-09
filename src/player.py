############################################################
#   PLAYER
############################################################

from printable import printable


class Player:

    def __init__(self, name, current_room=None):

        self.name = name
        self.current_room = current_room

    def __str__(self):

        attr_keys = ('name', 'current_room')

        return printable.to_str(self, attr_keys)

    def __repr__(self):

        attr_keys = ('name', 'current_room')

        return printable.to_repr(self, attr_keys)
