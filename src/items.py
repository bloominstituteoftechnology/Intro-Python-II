'''Add items to the game that the user can carry around'''
from room import Room

class Item(): 
    def __init__(self, name, description, location=None):
        self.name = name 
        self.description = description
        self.location = location