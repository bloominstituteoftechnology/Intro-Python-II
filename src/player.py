# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self. current_room = current_room
        self.inventory = []

   def __str__(self):
        plain = f"{self.name}\nInventory: "

        for i in self.items:
            plain += f"{i} "
        return plain

   