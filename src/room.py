# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)
        return self.items

    def delete_item(self, item):
        del self.items[item]

    def __str__(self):
        return f"{self.name}: {self.description}"