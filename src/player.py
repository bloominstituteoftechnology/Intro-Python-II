# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        # attributes
        self.name = name
        self.location = location

        self.current_location = current_location

    def __str__(self):
        return f"{self.name} is in the {self.location}"

    def set_location(self, current_location):
        self.current_location = current_location