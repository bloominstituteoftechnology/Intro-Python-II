# Implement a class to hold room information. This should have name and
# description attributes.

# which point to the room in that respective direction.

# Attributes
# name
# description

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return f"Room: {self.name}"
    def __repr__(self):
        return f"Room({repr(self.name, self.description)})"
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)