############################################################
#   ROOM
############################################################

from printable import printable


class Room:

    def __init__(self, name, description):

        self.name = name
        self.description = description

    def __str__(self):

        attr_keys = ('name', 'description')

        return printable.to_str(self, attr_keys)

    def __repr__(self):

        attr_keys = ('name', 'description')

        return printable.to_repr(self, attr_keys)
