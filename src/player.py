# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, guild, weapon, ability ):
        self.name = name
        self.guild = guild
        self.weapon = weapon
        self.ability = ability

    def __str__(self):
        output = f"Welcome {self.name}!"
        return output
        

player_1 = Player("Noraa Enidrev", "Dwarves Guild", "Battleaxe", "Armor Regeneration")

print(player_1)