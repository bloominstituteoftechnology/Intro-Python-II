# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name):
        # Initialize name and current_room during creation
        self.name = name
        self.current_room = None

    def set_room(self, room):
        self.current_room = room

    def get_room(self):
        return self.current_room

    def move(self, direction):
        current_room = self.get_room()
        try:
            if direction == 'n' and current_room.n_to:
                self.set_room(current_room.n_to)
                return True
            elif direction == 's' and current_room.s_to:
                self.set_room(current_room.s_to)
                return True
            elif direction == 'e' and current_room.e_to:
                self.set_room(current_room.e_to)
                return True
            elif direction == 'w' and current_room.w_to:
                self.set_room(current_room.w_to)
                return True
            else:
                return False
        except:
            return False
