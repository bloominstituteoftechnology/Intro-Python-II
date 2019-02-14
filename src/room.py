# Implement a class to hold room information. This should have name and
# description attributes.

from player import Player

class Room(Player):
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None):
        super().__init__(currentRoom, playerName)
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        return f"\nYou are currently in {self.name}.\n{self.description}"
        # return f"\n{playerName} are currently in {self.name}.\n{self.description}"
        
