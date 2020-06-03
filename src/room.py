'''
Creates a room object that has a name and a description
'''


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def _remove_item(self, item_name):
        return self.items.remove(item_name)

    def _add_item(self, item_name):
        self.items.append(item_name)

    def __str__(self):
        return 'The room is called: {self.name}.\n{self.description}'.format(self=self)

    def __repr__(self):
        return 'Room({self.name}, {self.description})'.format(self=self)
