from lib import Description

class Item(Description):
    """ This is a Room. """
    def __init__(self, name, description, storage=None):
        super().__init__(name, description, storage=storage)
    
    def __str__(self):
        return f'{self.name}: {self.description}'

    def __repr__(self):
        return f'Name: {self.name}\nDescription: {self.description}'