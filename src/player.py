# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return f'{self.name} is in {self.current_room}'

    def get_name(self):
        return str(self.name)

    def get_current_room(self, current_room):
        return str(self.current_room)

    def move_direction(self, direction):
        if direction == "n"
            self.current_room.n_to