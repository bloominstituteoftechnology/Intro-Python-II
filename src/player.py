# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        next_room = self.current_room.get_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("You can't move that way!!")
