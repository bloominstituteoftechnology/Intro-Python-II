# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        self.current_room = direction
        print(f'\nMoving to the {self.current_room.name}\n')