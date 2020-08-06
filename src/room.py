# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, n_to=[], s_to=[], e_to=[], w_to=[], items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        return (f"\nRoom Name: {self.name}\nDescription: {self.description}\n")

    def addItem(self, item):
        self.items = [*self.items]
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
