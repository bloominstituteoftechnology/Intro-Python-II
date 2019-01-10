# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:

    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location

    def __repr__(self):
        return f"{self.name} is in {self.current_location}."

    def set_current_location(self, new_location):
        self.current_location = new_location
