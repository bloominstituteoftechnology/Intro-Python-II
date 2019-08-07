# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def _init_(self, location):
        self.location = location

    def move_location(self, new_location):
        self.location = new_location

    def _repr_(self):
        return "Current Location: {}".format(self.location)

    def _str_(self):
        return "Current Location: {}".format(self.location)