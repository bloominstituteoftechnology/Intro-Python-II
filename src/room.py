# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def addItem(self, i):
        self.items.append(i)

    def __str__(self):
        return f"you find yourself at the {self.name}, {self.description}, in it lies {self.items}"
