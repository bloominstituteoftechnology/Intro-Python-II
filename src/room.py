# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = [] if items is None else items

    def drop_item(self, item):
        self.items.append(item)
    
    def take_item(self, item):
        self.items.remove(item)

    @property
    def inventory(self):
        return self.items

       