from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
     # Here we are describing our players attributes.
    def __init__(self, startLocation):
        self.location = startLocation
        self.items = []
    # Here we are defining the methods for the Player class

    def __repr__(self):
        return f"Player is in {self.location} "

    def findItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
