# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor
    def __init__(self, location):
        self.location = location
    # default representation
    def __repr__(self):
        return(f'Player is currently at the following location: {self.location}')
    