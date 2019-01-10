# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light


    def add_item(self, item):
        self.items.append(item)


    def remove_item(self, item):
        self.items.remove(item)


    def __repr__(self):
        return ": ".join((self.name, self.description))