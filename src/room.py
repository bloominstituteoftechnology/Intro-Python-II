from item import Item
from player import Player
# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    items = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def roomInDirection(self, direction):
        room = getattr(self, f"{direction}_to")
        if room is not None:
            return room
        else:
            return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def containsItem(self, item):
        return item in self.items

    def containsItemNamed(self, item):
        if self.itemNamed(item):
            return True
        else:
            return False

    def itemNamed(self, name):
        for item in self.items:
            lcName = item.name.lower()
            if name == lcName:
                return item

    def canEnter(self, player):
        return (True, "No lock")


class LockedRoom(Room):

    def __init__(self, name, description, requiredItemName):
        super().__init__(name, description)
        self.requiredItemName = requiredItemName

    def canEnter(self, player):
        item = player.itemNamed(self.requiredItemName)
        print(item)
        if item and player.holdingItem(item):
            return (True, f"The door was unlocked by {self.requiredItemName}.")
        else:
            return (False, "The door is locked.")