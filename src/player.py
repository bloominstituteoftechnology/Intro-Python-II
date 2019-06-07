# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        return f'Player is in {self.current_room}'

    def add_item(self, item):
        self.inventory.append(item)
    def get_name(self):
        return str(self.name)
    def get_current_room(self):
        return str(self.current_room)

    def move_direction(self, direction):
        if direction == "n":
            self.current_room.n_to
        elif direction == "s"
            self.current_room.s_to
        elif direction == "e"
            self.current_room.e_to
        elif direction == "w"
            self.current_room.w_to
        else:
            print("Invalid direction entered")