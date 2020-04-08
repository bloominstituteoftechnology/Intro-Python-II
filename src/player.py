############################################################
#   PLAYER
############################################################


class Player:

    def __init__(self, name, current_room):

        self.name = name
        self.current_room = current_room

    def __str__(self):

        class_name = self.__class__.__name__
        name = str(self.name)
        current_room = str(self.current_room)

        return ('\n'.join((
            f'{class_name} {{',
            f'    name: {name}',
            f'    current_room: {current_room}',
            f'}}',
        )))
        # -- I really don't like the hanging non-indentation in multi-line strings...

    def __repr__(self):

        class_name = self.__class__.__name__
        name = repr(self.name)
        current_room = repr(self.current_room)

        return (
            f'{class_name}({name}, {current_room})'
        )
