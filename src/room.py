# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, tool):
        self.name = name
        self.description = description
        self.tool = tool

    def __repr__(self):
        return "{self.__class__.__name__}({self.name}{self.description})".format(
            self=self
        )
