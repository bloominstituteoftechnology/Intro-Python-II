from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
     # Here we are describing our players attributes.
    def __init__(self, startLocation):
        self.location = startLocation
    # Here we are defining the methods for the Player class

    def change_location(self, new_location):
        self.location = new_location

    def pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):

        d = direction + "_to"

        # Checking to see if player can move a specific direction
        if not hasattr(self.location, d):
            print("You can't go that way!")
            return self.location
        else:
            self.location = self.location[d]
