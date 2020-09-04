# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items = []):
        self.name = name
        self.room = room
        self.items = items
    
    def __str__(self):
        return f"Player name: {self.name}, Room: {self.room}, Inventory Contains: {self.items}"

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)