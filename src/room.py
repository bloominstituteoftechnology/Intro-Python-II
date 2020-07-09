# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        # Print out name, descriptions, and items in room
        output = f'{self.name} contains items: '
        for i in self.items:
            output += f"\n {i}"
        output += f'\nCurrent location description: {self.description}'
        return output