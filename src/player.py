# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, description, fanny_pac, current):
        self.name = name
        self.description = description
        self.fanny_pac = fanny_pac
        self.current = current

    def __repr__(self):
        return "{self.__class__.__name__}({self.name}{self.fanny_pac}{self.current})".format(
            self=self
        )

