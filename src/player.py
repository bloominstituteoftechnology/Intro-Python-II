# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location="outside"):
        # attributes
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} is in the {self.location}"
