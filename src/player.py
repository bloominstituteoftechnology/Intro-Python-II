# Write a class to hold player information,
# e.g. what room they are in currently.


class Player():
    def __init__(self, location, items=[]):
        self.location = location
        self.items = items
