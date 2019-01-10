# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
wrapper = textwrap.TextWrapper()


class Room:
    def __init__(self, room, description, items):
        self.room = room
        self.description = description
        self.items = items

    def __repr__(self):
        desc = wrapper.wrap(self.description)
        string = '\n'
        for line in desc:
            string += line + '\n'
        string += 'Items: '
        if len(self.items) > 0:
            for i in self.items:
                string += i
        else:
            string += 'none'
        return string + '\n'
