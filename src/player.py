# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def __str__(self):
        return f"PLAYER NAME: {self.name} \n{self.location}"
