# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    
    def __str__(self):
        return (f"\nRoom Name: {self.name}\nDescription: {self.description}\n")

    def addItem(self, item):
        self.items = [*self.items]
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
