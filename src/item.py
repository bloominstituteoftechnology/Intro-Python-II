
class Item(object):
    '''
    A Simple item object
    Params -
        name - a string with the name of the room, keep it to one word
        description - a string with a description of the item is
    '''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def on_take(self):
        print(f'You have picked up {self.name}')

    def on_drop(self):
        print(f'You have dropped {self.name}')