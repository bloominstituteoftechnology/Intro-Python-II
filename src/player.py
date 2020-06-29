# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, guild, weapon, ability, current_room):
        self.name = name
        self.guild = guild
        self.weapon = weapon
        self.ability = ability
        self.current_room = current_room

    def __str__(self):
        output = f"Welcome {self.name}!\n Current Location: {self.current_room}"
        return output
    
    def __repr__(self):
        return f"Player: (self.name = {repr(self.name)}, self.current_room = {repr(self.current_room)})"
        

player_1 = Player("Noraa Enidrev", "Dwarves Guild", "Battleaxe", "Armor Regeneration")

print(player_1)