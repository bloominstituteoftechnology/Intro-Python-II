from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
     # Here we are describing our players attributes.
    def __init__(self, startLocation):
        self.location = startLocation
    # Here we are defining the methods for the Player class

    def __repr__(self):
        return f"Player is in {self.location} "
