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
            for (ind, item) in enumerate(self.items):
                if ind == 0 and len(self.items) < 1\
                        or ind == len(self.items) - 1:
                    items += f'{item.name} '
                else:
                    items += f'{item.name}, '
        else:
            items = 'none'

        desc = wrapper.wrap(self.description)
        items = wrapper.wrap(items)

        string = '\n'
        for line in desc:
            string += line + '\n'
        string += 'Room items: '
        for line in items:
            string += line + '\n'

        return string + '\n'

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
