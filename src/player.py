# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.currect_room = next_room
            print(f"*************************You entered {next_room}*************************")
        else:
            print("*************************You cannot move in that direction.*************************")