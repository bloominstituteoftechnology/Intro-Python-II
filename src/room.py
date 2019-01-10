# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
wrapper = textwrap.TextWrapper()


class Room:
    def __init__(self, room, description, items=[]):
        self.room = room
        self.description = description
        self.items = items

    def __repr__(self):
        items = ''
        if len(self.items) > 0:
            items = ' '.join(self.items)
        else:
            items = 'none'

        desc = wrapper.wrap(self.description)
        items = wrapper.wrap(items)

        string = '\n'
        for line in desc:
            string += line + '\n'
        string += 'Items: '
        for line in items:
            string += line + '\n'

        return string + '\n'
