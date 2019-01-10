# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''
     base class for player
    '''
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        # self.inventory = inventory
