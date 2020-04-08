############################################################
#   ROOM
############################################################


class Room:

    def __init__(self, name, description):

        self.name = name
        self.description = description

    def __str__(self):

        class_name = self.__class__.__name__
        name = str(self.name)
        description = str(self.description)

        return ('\n'.join((
            f'{class_name} {{',
            f'    name: {name}',
            f'    description: {description}',
            f'}}',
        )))
        # -- I really don't like the hanging non-indentation in multi-line strings...

    def __repr__(self):

        class_name = self.__class__.__name__
        name = repr(self.name)
        description = repr(self.description)

        return(
            f'{class_name}({name}, {description})'
        )
