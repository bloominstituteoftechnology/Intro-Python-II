# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """The main hero player for our text based adventure."""
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory