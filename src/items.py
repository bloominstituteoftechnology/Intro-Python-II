# Implement a class to hold item information. This should have name
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item: {self.name}'