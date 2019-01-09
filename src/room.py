# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
wrapper = textwrap.TextWrapper()


class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description

    def __repr__(self):
        desc = wrapper.wrap(self.description)
        string = ''
        for line in desc:
            string += line + '\n'
        return string
