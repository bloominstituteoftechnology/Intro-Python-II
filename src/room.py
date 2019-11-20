# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, playerName, description):
        self.playerName = playerName
        self.description = description
    
    def __str__(self):
        return f'Current Room: {self.playerName}, Room Description: {self.description}'

    name = str
    description = str

    n_to = str
    s_to = str
    w_to = str
    e_to = str