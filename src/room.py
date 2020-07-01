# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    """A class to hold room information and description attributes."""
    def __init__(self, name, description, n_to = None, e_to = None, s_to = None, w_to =None, items = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        plain = f"Current Room: {self.name} {self.description}\n"

        for i in self.items:
            plain = f"Available Items: {i}. {i.description}"
        return plain

   

    