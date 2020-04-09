# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def takeItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item)
