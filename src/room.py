# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

        self.items: [Item] = []

    def __str__(self):
        result = 'You are at {self.name}. {self.description}\n'.format(self=self)

        if len(self.items) > 0:
            result = result + "\nThe following items are in the room:\n"
        for i in self.items:
            result = result + f"{i.name}: {i.description}\n"
        return result
