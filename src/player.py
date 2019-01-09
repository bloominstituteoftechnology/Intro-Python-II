from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = []

    def pickup_item(self, item):
        self.inventory.append(item)
    
    def try_move(self, direction):
        d = direction + "_to"

        if not hasattr(self.currentRoom, d):
            print("you can't go that way")
            return self.currentRoom
        else:
            self.currentRoom[d]


