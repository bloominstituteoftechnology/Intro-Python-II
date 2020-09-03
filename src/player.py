# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, direction):
        attribute = direction + '_to'
        if hasattr(self.location, attribute):
            self.location = getattr(self.location, attribute)
        else:
            print("You can't go there.")
