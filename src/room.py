# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_items(self, *item):
        for i in item:
            self.items.append(i)

    def __str__(self):
        return f"Name: {self.name}, description: {self.description}, Items: {self.items}"