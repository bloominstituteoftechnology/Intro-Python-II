# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __repr__(self):
        return f"Player Name: {self.name}, Current Room: {self.current_room}, Items in Inventory: {self.inventory}"
