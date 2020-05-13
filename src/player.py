# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, locations):
        self.name = name
        self.locations = []

        for x in locations:
            location = Room(x)
            self.locations.append(location)
