# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def __str__(self):
        return f'{self.name}, you are at the {self.current_room}'

    # take item

    # drop item
