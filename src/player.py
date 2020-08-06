# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
​
    def try_direction(self, command):
        attribute = command  + '_to'
​
        # see if the current room has the attribute 
        # we can use a Python function called `hasattr`
        if hasattr(self.location, attribute):
            # use `getattr` to actually move to the room 
            self.location = getattr(self.location, attribute)
        else:
            print("You can't go that way!\n")