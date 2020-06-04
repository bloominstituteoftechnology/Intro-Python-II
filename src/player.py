# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, starting_room)
        self.name = name
        self.current_room = starting_room

    def movement(self, inp):
        if inp == "q"
            print("Thank you for playing! Goodbye!")
            return True
            # Returns True to quit game

        else:
            possible_room