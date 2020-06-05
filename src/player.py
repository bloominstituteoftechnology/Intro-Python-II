# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        return f'{self.name}, you are at the {self.current_room}'

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)