# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"Player: {self.name}, {self.room}"

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        del self.inventory[item]
