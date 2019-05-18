# This is the base class for items in the game.

class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __getitem__(self, key):
        self_object = {
            'name': self.name,
            'value': self.value
        }
        return self_object

    def __str__(self):
        return self.name
