# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items = []):
        self.name = name
        self.room = room
        self.items = []
    
    def print_items(self):
        if self.items == []:
            return
        else:
            print(f"You have the following items: {self.items}")
