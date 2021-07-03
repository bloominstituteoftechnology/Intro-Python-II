# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory = [] * 2):
        self.name = name
        self.location = location
        self.inventory = inventory

    def __repr__(self):
        return f"{self.name} is in {self.location}"

