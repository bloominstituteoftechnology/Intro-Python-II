# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        self.happiness = 1

    def print_item_names(self):
        return [item.name for item in self.items]

    def __repr__(self):
        return f"Player is in {self.current_room.name} \n Inventory: {self.print_item_names()}"
