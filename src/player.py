from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    items = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def changeRoom(self, room):
        self.current_room = room

    def pickUpItem(self, item):
        if len(self.items) >= 2:
            print("You can only hold two items at a time! (Two hands, after all) Set something down first.")
        else:
            self.current_room.removeItem(item)
            self.items.append(item)
            item.onTake()

    def setDownItem(self, item):
        if self.holdingItem(item):
            self.items.remove(item)
            self.current_room.addItem(item)
            item.onDrop()

    def holdingItem(self, item):
        return item in self.items
