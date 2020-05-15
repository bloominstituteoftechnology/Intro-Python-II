# Write a class to hold player information, e.g. what room they are in
# currently.
"""
Ready Player 1

Attributes:
-name
-current_room
"""

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        
    def __str__(self):
       return f"Player Name: {self.name} \nPlayers {self.room}"
