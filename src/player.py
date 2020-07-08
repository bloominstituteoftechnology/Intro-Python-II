# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def movePlayer(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(
                self.current_room, f'{direction}_to'
            )
        else:
            print()
            print("There doesn't seem to be anything in that direction")
            