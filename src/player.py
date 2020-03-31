# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def try_north(self):
        if self.current_room.n_to != None:
            self.current_room = self.current_room.n_to
        else:
            print("**You can't go north from this room. Please enter a different direction.**")

    def try_south(self):
        if self.current_room.s_to != None:
            self.current_room = self.current_room.s_to
        else:
            print("**You can't go south from this room. Please enter a different direction.**")

    def try_east(self):
        if self.current_room.e_to != None:
            self.current_room = self.current_room.e_to
        else:
            print("**You can't go east from this room. Please enter a different direction.**")

    def try_west(self):
        if self.current_room.w_to != None:
            self.current_room = self.current_room.w_to
        else:
            print("**You can't go west from this room. Please enter a different direction.**")