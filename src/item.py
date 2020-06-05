# Implement a class to hold item information. This should have name and
# description attributes.

class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        result = 'You\'re holding a {self.name}. {self.description}\n'.format(self=self)
        return result
