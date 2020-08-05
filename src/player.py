# Write a class to hold player information, e.g. what room they are in
# currently.

import textwrap

class Player:

    # determines if player can move to a room
    new_room = True

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # method to print out players current location
    def location(self):
        if self.new_room == True:
            print(f"You are currently in {self.current_room.name}")
            for des in textwrap.wrap(self.current_room.description):
                print(des)

    # method to determine which way the player chooses to move
    # and if they can go that way.
    def moveTo(self, direction):
        self.new_room = False
        if direction == 'n' and self.current_room.n_to != 0:
            self.current_room = self.current_room.n_to
            self.new_room = True
        elif direction == 'e' and self.current_room.e_to != 0:
            self.current_room = self.current_room.e_to
            self.new_room = True
        elif direction == 's'and self.current_room.s_to != 0:
            self.current_room = self.current_room.s_to
            self.new_room = True
        elif direction == 'w' and self.current_room.w_to != 0:
            self.current_room = self.current_room.w_to
            self.new_room = True
        else:
            print("Can't move in that direction, choose another option (n,e,s,w)")