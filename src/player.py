# Write a class to hold player information, e.g. what room they are in
# currently.

# need to define a player dict somewhere

class Player: 
    
    def __init__(self, current_room, player_info):
        self.current_room=current_room
        self.player_info=player_info # pretty sure this would be a dict indicating what they are holding
    
    def __str__():

        return f"{self.current_room} {self.player_info}"
