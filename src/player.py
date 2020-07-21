# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        
    def __str__(self):
        readable = f"{self.name}\n Inventory: "

        for i in self.items:
            readable += f"{i} "
        return readable