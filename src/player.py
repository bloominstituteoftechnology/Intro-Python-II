# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, player_name, in_room):
        self.player_name = player_name
        self.in_room = in_room
    
    def __str__(self):
        return f'{self.player_name} is in {self.in_room}'
