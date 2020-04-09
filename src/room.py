# Implement a class to hold room information. This should have name and
# description attributes.

import room
from item import Item


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = 0
        self.e_to = 0
        self.s_to = 0
        self.w_to = 0

    def check(self):
        print(f'Items in this room : {self.items}')

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)



    def tryToMove(self, move, stringInput, check):
        if move == stringInput:
            if(check == 0):
                print("\nERROR: Can't move that direction here.")
                return False
            else:
                return True

        



    def playerMove(self, direction):

        return (self.tryToMove(direction, "n", self.n_to) or 
                self.tryToMove(direction, "e", self.e_to) or
                self.tryToMove(direction, "s", self.s_to) or
                self.tryToMove(direction, "w", self.w_to))

    def __str__(self):
        return (self.description + "\nLocation: \"" + self.name + "\"")

    def __repr__(self):
        return ("\nEntered " + self.name + ". " + self.description)
 