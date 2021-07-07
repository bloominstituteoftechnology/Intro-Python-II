from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name, current_room, inventory=[]):
        self.player_name = player_name
        self.current_room = current_room
        self.inventory = inventory
        

"""    def __repr__(self):
        return f'{self.playerName}, you are in the {}'"""