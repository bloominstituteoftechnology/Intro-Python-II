# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''A room the player can enter'''
    def __init__(self, name, description):
        self.name = name
        self.description = description
