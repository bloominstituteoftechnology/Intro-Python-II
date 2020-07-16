# Implement a class to hold room information. This should have name and
# description attributes.
import random
from utils import clear

class Room:
    def __init__(self, name, desc, items=None):
        self.name = name
        self.desc = desc
        self.items = items
    def __getitem__(self, name):
        return getattr(self, name)
    def list_items(self):
        items = ", ".join([name.__str__() for name in self.items.keys()])
        return items
    def get_item(self, item_name):
        if self.items[item_name]:
            found_item = self.items[item_name]
            self.items.pop(item_name)
            return found_item
        return False