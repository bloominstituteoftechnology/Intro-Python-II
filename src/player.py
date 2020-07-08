# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if self.current_room.move[direction] is not None:
            self.current_room = self.current_room.move[direction]
        else:
            print("Try a different direction!")

    def pickup_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)