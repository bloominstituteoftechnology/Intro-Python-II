############################################################
#   ROOM
############################################################

from printable import printable


class Room:

    directions = ('n', 'e', 's', 'w')
    connections = tuple(f'{dir}_to' for dir in directions)

    def __init__(self, name, description=None, **kwargs):

        self.name = name
        self.description = description

        # parse kwargs for keys in connections
        for move_key in self.connections:

            move_value = None

            if move_key in kwargs.keys():
                move_value = kwargs[move_key]

            setattr(self, move_key, move_value)

        return

    def __str__(self):

        attr_keys = ('name', 'description', *self.connections)

        return printable.to_str(self, attr_keys)

    def __repr__(self):

        attr_keys = ('name', 'description')

        return printable.to_repr(self, attr_keys)
