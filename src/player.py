from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def pickup_item(self, item):
        self.inventory.append(item)
    
    def try_move(self, direction):
        attribute = str(direction) + "_to"

        if not hasattr(self.current_room, attribute):
            print("you can't go that way")
            return self.current_room
        else:
            new_room = getattr(self.current_room, attribute)
            return new_room


