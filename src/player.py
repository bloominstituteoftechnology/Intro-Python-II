# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''
     base class for player
    '''
    def __init__(self, currentRoom, inventory):
        self.currentRoom = currentRoom
        self.inventory = inventory
