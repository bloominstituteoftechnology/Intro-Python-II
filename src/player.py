# Write a class to hold player information, e.g. what room they are in
# currently.


class Room:
    def __init__(self, name, location, inv, health):
        self.name = name
        self.location = location
        self.inv = inv
        self.health = health
