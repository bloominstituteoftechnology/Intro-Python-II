# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if len(self.items) == 2:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> {self.items[0]} and {self.items[1]}'
        elif len(self.items) == 1:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> {self.items[0]}'
        else:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> None'

    def remove_item(self, item):
        self.items.remove(item)