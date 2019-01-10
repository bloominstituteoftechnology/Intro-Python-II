# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''
     base class for player
    '''
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # self.inventory = inventory

    def __repr__(self):
        return (f'{self.name} is currently in {self.current_room}.')
