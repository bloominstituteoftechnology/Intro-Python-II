# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, mana, backpack, player_type, hp):
        self.location = location
        self.mana = mana
        self.backpack = backpack
        self.player_type = player_type
        self.hp = hp
