# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    def __init__(self, name, desc, items=None):
        self.name = name
        self.desc = desc
        self.items = items
    def __getitem__(self, name):
        return getattr(self, name)
    def get_item(self):
        if self.items:
            item = random.choice(self.items)
            self.items.remove(item)
            return item
        print('There are no items in this room.')
        return False