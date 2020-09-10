# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    
    def move(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to', None)

        if next_room is not None:
            self.current_room = next_room
        else:
            print("\n")
            print("You can't move that way")