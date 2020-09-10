# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'

    def move(self, direction):
        if self.current_room.__call__(direction) == None:
            print(f"You cannot go in that direction, you are staying in {self.current_room.name}")
        else:
            self.current_room = self.current_room.__call__(direction)
            return  self.current_room