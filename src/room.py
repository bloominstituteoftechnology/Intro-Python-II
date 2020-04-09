############################################################
#   ROOM
############################################################

from printable import printable


class Room:

    ########################################
    #   properties
    ########################################

    directions = ('n', 'e', 's', 'w')
    connections = tuple(f'{dir}_to' for dir in directions)

    @property
    def n_to(self): return self.__n_to

    @n_to.setter
    def n_to(self, value): self.__n_to = value

    @property
    def e_to(self): return self.__e_to

    @e_to.setter
    def e_to(self, value): self.__e_to = value

    @property
    def s_to(self): return self.__s_to

    @s_to.setter
    def s_to(self, value): self.__s_to = value

    @property
    def w_to(self): return self.__w_to

    @w_to.setter
    def w_to(self, value): self.__w_to = value

    ########################################
    #   dunders
    ########################################

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
