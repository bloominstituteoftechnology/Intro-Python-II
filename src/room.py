from item import Item
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
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
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
