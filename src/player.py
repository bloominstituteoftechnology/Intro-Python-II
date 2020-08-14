# from inventory import inventory
# # Write a class to hold player information, e.g. what room they are in
# # currently.

# # need to define a player dict somewhere

# player_info = {

#     "name": "Player",
#     'player_inventory': inventory
#     # coordinates: {{'x': 0}
#     #                {'y': 0}}

# }


class Player: 
    
    def __init__(self, current_room, name):
        self.current_room=current_room
        self.name=name
        # self.player_info=player_info # pretty sure this would be a dict indicating what they are holding
    
    def __str__(self):
        return f"{self.current_room} {self.player_info}"