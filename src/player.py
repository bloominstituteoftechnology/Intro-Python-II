# Write a class to hold player information, e.g. what room they are in
# currently.
# note that room and player has items 
class Player:


    from item import Item
    from room import Room
    def __init__(self, name, currentRoom: Room):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def pick_item(self, item):
        self.inventory.append(item)

        
    def pickup_item(self, item):
        if item is not None:
            self.inventory.append(item)
            item.on_take()

    def drop_item(self, item):
        self.inventory.remove(item)